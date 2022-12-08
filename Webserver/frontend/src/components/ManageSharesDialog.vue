<template>

    <v-dialog v-model="visible">

        <v-card>
            <v-card-title>Personen mit Zugriff auf Ihre Daten</v-card-title>
            <v-card-text>
                <div v-if="errorMessage != null">
                    Die Daten konnten nicht geladen werden.<br />
                    {{ errorMessage }}
                </div>
                <div v-else-if="activeShares == null">
                    Daten werden abgerufen...
                </div>
                <div v-else-if="activeShares.length === 0">
                    Sie haben noch keine Dateifreigaben eingerichtet.
                </div>
                <v-simple-table v-else>
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left">Freigegebene Datei / Ordner</th>
                                <th class="text-left">Benutzer</th>
                                <th style="width: min(20vw, 160px);"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="share in activeShares" :key="share.id">
                                <td class="text-left">{{ share.path }}</td>
                                <td class="text-left">{{ share.subjectName }}</td>
                                <td>
                                    <v-btn color="red" v-on:click="deleteShare(share)">Entfernen</v-btn>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-spacer />
                <v-btn color="secondary" v-on:click="hide()" text>Schließen</v-btn>
            </v-card-actions>
        </v-card>

    </v-dialog>

</template>

<script>

    import * as fileservice from "@/fileservice";

    async function loadData() {
        const userinfo = (await fileservice.getUserInfo()).userinfo;
        return await Promise.all(userinfo.ownShares.map(async rawShare => {
            const share = (await fileservice.getShare(rawShare.id)).share;
            return {
                id: share.id,
                path: await getSharePath(share),
                subjectName: share.subject.displayName
            }
        }));
    }

    async function getSharePath(share) {
        let name;
        let nextParentID;
        if(share.target.type === "directory") {
            name = "";
            nextParentID = share.target.id;
        } else {
            name = share.target.file.name;
            nextParentID = share.target.file.parentDirectory;
        }
        for(;;) {
            let nextParent = (await fileservice.getDirectory(nextParentID)).directory;
            if(nextParent.parentDirectory == null)
                return "/Eigene Dateien/" + name;
            nextParentID = nextParent.parentDirectory;
            name = nextParent.name + "/" + name;
        }
    }

    export default {
        name: "manage-shares-dialog",
        props: {
            displayMessage: Function
        },
        data: () => ({
            visible: false,
            closing: false,
            errorMessage: null,
            activeShares: null
        }),
        methods: {
            show() {
                loadData()
                    .then(data => this.activeShares = data)
                    .catch(err => {
                        console.log(err);
                        this.errorMessage = err;
                    })
                this.visible = true;
            },
            hide() {
                this.closing = true;
                this.visible = false;
                this.errorMessage = null;
                this.activeShares = null;
                this.closing = false;
            },
            deleteShare(activeShare) {
                fileservice.deleteShare(activeShare.id)
                  .then(() => {
                    const index = this.activeShares.indexOf(activeShare);
                    if(index >= 0)
                        this.activeShares.splice(index, 1);
                  })
                  .catch(err => this.displayMessage({message: "Failed to delete share with ID " + activeShare.id, userMessage: "Beim Löschen der Freigabe ist ein Fehler aufgetreten."}, err))
            }
        },
        watch: {
            visible: function() {
                if(!this.visible && !this.closing)
                    this.hide();
            }
        }
    };

</script>
