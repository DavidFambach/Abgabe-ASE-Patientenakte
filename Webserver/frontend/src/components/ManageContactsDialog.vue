<template>

    <v-dialog v-model="visible">

        <v-card>
            <v-card-title>Kontakte verwalten</v-card-title>
            <v-card-text>
                <p>
                    Fügen Sie Personen, mit denen Sie ihrer Dateien teilen möchten, unten hinzu. Danach
                    können Sie einzelne Dateien und Ordner mit diesen Personen teilen. Um Kontakte
                    hinzuzufügen, benötigen Sie einmalig die Benutzernummer, die Ihnen von Ihrem Kontakt
                    mitgeteilt wird.
                </p>
                <p v-if="errorMessage != null">
                    Die Daten konnten nicht geladen werden.<br />
                    {{ errorMessage }}
                </p>
                <p v-else-if="contacts == null">
                    Daten werden abgerufen...
                </p>
                <p v-else-if="contacts.length === 0">
                    Sie haben noch keine Kontakte.
                </p>
                <v-simple-table v-else>
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left">Bestehende Kontakte</th>
                                <th style="width: min(20vw, 160px);"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="contact in contacts" :key="contact.id">
                                <td class="text-left">{{ contact.name }}</td>
                                <td>
                                    <v-btn color="red" v-on:click="deleteContact(contact)">Entfernen</v-btn>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
                <v-divider class="mb-4" />
                <v-simple-table>
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left">Neuen Kontakt hinzufügen</th>
                                <th style="width: min(20vw, 160px);"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <v-text-field label="Benutzernummer des Kontakts" placeholder="12345678"
                                        color="secondary" v-model="addContactID" />
                                </td>
                                <td>
                                    <v-btn color="green"
                                        :disabled="addContactID == '' || addContactPending || addContactInfo == null"
                                        :outlined="addContactID == '' || addContactPending || addContactInfo == null"
                                        v-on:click="addContact(addContactInfo)">Hinzufügen</v-btn>
                                </td>
                            </tr>
                            <tr v-if="addContactID != '' && addContactPending">
                                <td colspan="2">
                                    <i>Benutzer wird gesucht...</i>
                                </td>
                            </tr>
                            <tr v-else-if="addContactID != '' && addContactInfo == null">
                                <td colspan="2" class="red--text">
                                    <b>Diese Benutzernummer ist nicht gültig.</b>
                                </td>
                            </tr>
                            <tr v-else-if="addContactID != '' && addContactInfo != null && contacts.map(c => c.id).includes(addContactInfo.id)">
                                <td colspan="2" class="red--text">
                                    <b>Der Benutzer "{{ addContactInfo.name }}" ist bereits in ihrer Kontaktliste.</b>
                                </td>
                            </tr>
                            <tr v-else-if="addContactID != '' && addContactInfo != null">
                                <td colspan="2">
                                    <b>Benutzer: </b>{{ addContactInfo.name }}
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
        return userinfo.contacts.map(contact => {
            return {
                id: contact.id,
                name: contact.displayName
            }
        });
    }

    export default {
        name: "manage-contacts-dialog",
        props: {
            displayMessage: Function
        },
        data: () => ({
            visible: false,
            closing: false,
            errorMessage: null,
            contacts: null,
            addContactID: "",
            addContactPending: false,
            addContactModCount: 0,
            addContactInfo: null
        }),
        methods: {
            show() {
                loadData()
                    .then(data => this.contacts = data)
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
                this.contacts = null;
                this.closing = false;
            },
            addContact(contact) {
                if(this.contacts.map(c => c.id).includes(contact.id))
                    return;
                fileservice.addContact(contact.id)
                    .then((contactResponse) => {
                        if(!this.contacts.map(c => c.id).includes(contact.id)) {
                            this.contacts.push({
                                id: contactResponse.contact.id,
                                name: contactResponse.contact.displayName
                            });
                        }
                        if(this.addContactID == contactResponse.contact.id)
                            this.addContactID = "";
                    }).catch(err => {
                        if(err.body != null && err.body.status === "invalid_contact")
                            this.displayMessage({message: "Failed to add contact with ID " + contact.id, userMessage: "Sie können sich nicht selbst als Kontakt hinzufügen."}, err);
                        else
                            this.displayMessage({message: "Failed to add contact with ID " + contact.id, userMessage: "Beim Hinzufügen des Kontakts ist ein Fehler aufgetreten."}, err);
                    })
            },
            deleteContact(contact) {
                if(!this.contacts.map(c => c.id).includes(contact.id))
                    return;
                fileservice.removeContact(contact.id)
                    .then(() => {
                        const index = this.contacts.map(c => c.id).indexOf(contact.id);
                        if(index >= 0)
                            this.contacts.splice(index, 1);
                    }).catch(err => this.displayMessage({message: "Failed to delete contact with ID " + contact.id, userMessage: "Beim Löschen des Kontakts ist ein Fehler aufgetreten."}, err))
            }
        },
        watch: {
            visible: function() {
                if(!this.visible && !this.closing)
                    this.hide();
            },
            addContactID: function() {
                this.addContactModCount++;
                if(!this.addContactID.match(/^[1-9][0-9]*$/)) {
                    this.addContactPending = false;
                    this.addContactName = null;
                    return;
                }
                this.addContactPending = true;
                const expectedModCount = this.addContactModCount;
                fileservice.getContactName(this.addContactID)
                    .then((contactResponse => {
                        if(expectedModCount !== this.addContactModCount)
                            return;
                        this.addContactPending = false;
                        this.addContactInfo = {
                            id: contactResponse.contact.id,
                            name: contactResponse.contact.displayName
                        };
                    }).bind(this)).catch((err => {
                        if(err.body == null || err.body.status !== "not_found")
                            console.log(err);
                        if(expectedModCount !== this.addContactModCount)
                            return;
                        this.addContactPending = false;
                        this.addContactInfo = null;
                    }).bind(this));
            }
        }
    };

</script>
