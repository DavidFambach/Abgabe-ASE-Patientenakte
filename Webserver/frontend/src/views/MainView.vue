
<template>
  <v-app>

    <manage-contacts-dialog ref="manageContactsDialog" :displayMessage="displayMessage"/>
    <manage-shares-dialog ref="manageSharesDialog" :displayMessage="displayMessage"/>
    <main-navigation-bar :displayMessage="displayMessage"
      :openContactsDialog="() => $refs.manageContactsDialog.show()"
      :openShareDialog="() => $refs.manageSharesDialog.show()" />

    <v-main class="grey lighten-3">
        <v-row>
          <v-col cols="2">
            <v-sheet >
              <v-list color="transparent">
                  <v-list-item-group
                  v-model="selectedDisplayModeID"
                  background-color="secondary"
                  >
                <v-list-item v-on:click="setActiveView(CONST.DISPLAY_MODE_OWN_FILES)">
                  <v-list-item-content>
                    <v-list-item-title>
                      Eigene Dateien
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item v-on:click="setActiveView(CONST.DISPLAY_MODE_SHARED_FILES)">
                  <v-list-item-content>
                    <v-list-item-title>
                      Mit mir geteilt
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>
          
          <v-col>
            <v-sheet
              width="95%"
              rounded="lg"
            >

            <v-treeview :items="displayedListEntries" :load-children="loadEntries"
              :open.sync="displayedListEntriesOpen" item-disabled="disabled"
              open-on-click hoverable dense
              ref="fileTree">
              <template v-slot:label="{ item }">
                <v-row>
                  <v-col class="flex-grow-1 my-auto">{{ item.name }}</v-col>
                  <v-col v-if="'owner' in item" class="text-right my-auto">{{ item.owner }}</v-col>
                  <v-col class="text-right flex-grow-0" style="min-width: 240px;">
                    
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_UPLOAD_FILE)"
                      v-on:click.stop="dialogs.uploadFileDialog.dialog.open('Datei hochladen', 'Wählen Sie Dateien zum Hochladen aus:', [{text: 'Abbrechen'}, {text: 'Hochladen', color: 'green', onclick: () => triggerAction(CONST.ACTION_UPLOAD_FILE, {targetNode: item})}])">
                      <v-icon>mdi-file-upload-outline</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_CREATE_DIRECTORY)"
                      v-on:click.stop="dialogs.createDirectoryDialog.dialog.open('Neues Verzeichnis erstellen', 'Geben Sie einen Verzeichnisnamen ein:', [{text: 'Abbrechen'}, {text: 'Erstellen', color: 'green', onclick: () => triggerAction(CONST.ACTION_CREATE_DIRECTORY, {targetNode: item})}])">
                      <v-icon>mdi-folder-plus</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_RENAME_DIRECTORY)"
                      v-on:click.stop="dialogs.renameDialog.dialog.open('Verzeichnis umbenennen', 'Geben Sie einen neuen Verzeichnisnamen ein:', [{text: 'Abbrechen'}, {text: 'Umbenennen', color: 'green', onclick: () => triggerAction(CONST.ACTION_RENAME_DIRECTORY, {targetNode: item})}])">
                      <v-icon>mdi-folder-edit</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_SHARE_DIRECTORY)"
                      v-on:click.stop="dialogs.createShareDialog.targetsDirectory = true; dialogs.createShareDialog.dialog.open('Verzeichnis freigeben', 'Wählen Sie einen Kontakt, mit dem Sie das Verzeichnis &quot;' + item.name + '&quot; teilen möchten:', [{text: 'Abbrechen'}, {text: 'Freigeben', color: 'green', onclick: () => triggerAction(CONST.ACTION_SHARE_DIRECTORY, {targetNode: item})}])">
                      <v-icon>mdi-share-all</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_MOVE_DIRECTORY)"
                      v-on:click.stop="dialogs.moveDialog.dialog.open('Verzeichnis verschieben', 'Wählen Sie ein Verzeichnis, in das das Verzeichnis verschoben werden soll:', [{text: 'Abbrechen'}, {text: 'Verschieben', color: 'green', onclick: () => triggerAction(CONST.ACTION_MOVE_DIRECTORY, {targetNode: item})}])">
                      <v-icon>mdi-folder-move</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_DELETE_DIRECTORY)"
                      v-on:click.stop="dialogs.confirmDeleteDirectory.dialog.open('Löschen bestätigen', 'Möchten Sie das Verzeichnis &quot;' + item.name + '&quot; löschen?', [{text: 'Abbrechen'}, {text: 'Löschen', color: 'red', onclick: () => triggerAction(CONST.ACTION_DELETE_DIRECTORY, {targetNode: item})}])">
                      <v-icon>mdi-folder-minus</v-icon>
                    </v-btn>
                    
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_DOWNLOAD_FILE)"
                      v-on:click.stop="triggerAction(CONST.ACTION_DOWNLOAD_FILE, {targetNode: item})">
                      <v-icon>mdi-file-download-outline</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_RENAME_FILE)"
                      v-on:click.stop="dialogs.renameDialog.dialog.open('Datei umbenennen', 'Geben Sie einen neuen Dateinamen ein:', [{text: 'Abbrechen'}, {text: 'Umbenennen', color: 'green', onclick: () => triggerAction(CONST.ACTION_RENAME_FILE, {targetNode: item})}])">
                      <v-icon>mdi-file-edit-outline</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_SHARE_FILE)"
                      v-on:click.stop="dialogs.createShareDialog.targetsDirectory = false; dialogs.createShareDialog.dialog.open('Datei freigeben', 'Wählen Sie einen Kontakt, mit dem Sie die Datei &quot;' + item.name + '&quot; teilen möchten:', [{text: 'Abbrechen'}, {text: 'Freigeben', color: 'green', onclick: () => triggerAction(CONST.ACTION_SHARE_FILE, {targetNode: item})}])">
                      <v-icon>mdi-share</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_MOVE_FILE)"
                      v-on:click.stop="dialogs.moveDialog.dialog.open('Datei verschieben', 'Wählen Sie ein Verzeichnis, in das die Datei verschoben werden soll:', [{text: 'Abbrechen'}, {text: 'Verschieben', color: 'green', onclick: () => triggerAction(CONST.ACTION_MOVE_FILE, {targetNode: item})}])">
                      <v-icon>mdi-file-move-outline</v-icon>
                    </v-btn>
                    <v-btn icon v-if="'object' in item && item.object.permittedActions.includes(CONST.ACTION_DELETE_FILE)"
                      v-on:click.stop="dialogs.confirmation.dialog.open('Löschen bestätigen', 'Möchten Sie die Datei &quot;' + item.name + '&quot; löschen?', [{text: 'Abbrechen'}, {text: 'Löschen', color: 'red', onclick: () => triggerAction(CONST.ACTION_DELETE_FILE, {targetNode: item})}])">
                      <v-icon>mdi-file-minus-outline</v-icon>
                    </v-btn>

                  </v-col>
                </v-row>
              </template>
              <template v-slot:prepend="{ item, open }">
                <v-icon v-if="'object' in item && item.object.type === 'directory'">
                  {{ open ? "mdi-folder-open" : "mdi-folder" }}
                </v-icon>
                <v-icon v-else-if="'displayIcon' in item">
                  {{ item.displayIcon }}
                </v-icon>
              </template>
            </v-treeview>

            </v-sheet>
          </v-col>
        </v-row>
        
        <action-dialog ref="confirmationDialog" />
        <action-dialog ref="confirmationDialogDeleteDirectory"
          :prepare="() => {dialogs.confirmDeleteDirectory.cascade = false;}">
          <template v-slot:extra>
            <v-checkbox v-model="dialogs.confirmDeleteDirectory.cascade" :label="'Verzeichnisinhalt löschen'"
              color="red"/>
          </template>
        </action-dialog>
        <action-dialog ref="uploadFileDialog"
          :prepare="() => {dialogs.uploadFileDialog.selectedFiles = []}">
          <template v-slot:extra>
            <v-file-input counter multiple show-size
              v-model="dialogs.uploadFileDialog.selectedFiles" placeholder="Dateien auswählen"
              color="secondary" truncate-length="50" />
          </template>
        </action-dialog>
        <action-dialog ref="createDirectoryDialog"
          :prepare="() => {dialogs.createDirectoryDialog.directoryName = 'Neues Verzeichnis';}">
          <template v-slot:extra>
            <v-text-field label="Name" placeholder="Verzeichnisname" color="secondary"
              v-model="dialogs.createDirectoryDialog.directoryName"/>
          </template>
        </action-dialog>
        <action-dialog ref="createShareDialog"
          :prepare="prepareShareDialog">
          <template v-slot:extra>
            <br />
            <template v-if="dialogs.createShareDialog.contactsByName != null">
              <template v-if="Object.keys(dialogs.createShareDialog.contactsByName).length > 0">
                <v-select label="Kontakt" color="secondary" dense
                  :items="Object.keys(dialogs.createShareDialog.contactsByName)"
                  v-model="dialogs.createShareDialog.selectedContactName">
                </v-select>
                <v-checkbox v-model="dialogs.createShareDialog.writePermission" :label="'Schreibberechtigung erteilen'"
                  color="secondary"/>
                <p v-if="dialogs.createShareDialog.targetsDirectory">
                  Wenn Sie dem Benutzer Schreibberechtigungen erteilen, kann er in diesem Verzeichnis
                  neue Dateien und Verzeichnisse anlegen sowie Unterverzeichnisse und Dateien verändern
                  oder löschen.
                </p>
                <p v-else>
                  Wenn Sie dem Benutzer Schreibberechtigungen erteilen, kann er den Inhalt der Datei
                  überschreiben. Er kann die Datei nur umbenennen oder löschen, wenn er auch eine
                  Schreibberechtigung für das Verzeichnis hat, in dem sich die Datei befindet.
                </p>
              </template>
              <template v-else>
                Sie haben noch keine Kontakte.<br />
                Wechseln Sie zum Reiter
                <v-btn color="secondary" text x-small
                  v-on:click.stop="() => {
                    dialogs.createShareDialog.dialog.close();
                    $refs.manageContactsDialog.show();
                  }">
                  Kontakte verwalten
                </v-btn>
                , um Kontakte hinzuzufügen.
              </template>
            </template>
            <template v-else>
              Kontakte werden geladen...
            </template>
          </template>
        </action-dialog>
        <action-dialog ref="renameDialog"
          :prepare="() => {dialogs.renameDialog.newName = '';}">
          <template v-slot:extra>
            <v-text-field label="Neuer Name" placeholder="Unbenannt" color="secondary"
              v-model="dialogs.renameDialog.newName"/>
          </template>
        </action-dialog>
        <action-dialog ref="moveDialog"
          :prepare="() => {dialogs.moveDialog.options = calculateMoveTargets();dialogs.moveDialog.targetDirectory = '';}">
          <template v-slot:extra>
            <br />
            <v-select label="Zielverzeichnis" color="secondary" dense
              :items="Object.keys(dialogs.moveDialog.options)"
              v-model="dialogs.moveDialog.seletectedTarget">
            </v-select>
          </template>
        </action-dialog>

        <snackbar-helper ref="snackbar" />

    </v-main>
  </v-app>
</template>

<script>
  import ActionDialog from '@/components/ActionDialog.vue';
  import MainNavigationBar from '@/components/MainNavigationBar.vue';
  import ManageContactsDialog from '@/components/ManageContactsDialog.vue';
  import ManageSharesDialog from '@/components/ManageSharesDialog.vue';
  import SnackbarHelper from '@/components/SnackbarHelper.vue';
  import * as fileservice from "@/fileservice";
  import * as session from "@/session";
  import { readFileToBlob } from "@/util";

  const FILE_ICONS = {
    "": "mdi-file-outline",
    "doc": "mdi-file-document-outline",
    "docm": "mdi-file-document-outline",
    "docx": "mdi-file-document-outline",
    "dotm": "mdi-file-document-outline",
    "dotx": "mdi-file-document-outline",
    "gif": "mdi-file-gif-box",
    "go": "mdi-language-go",
    "html": "mdi-language-html5",
    "java": "mdi-language-java",
    "jpeg": "mdi-file-image",
    "jpg": "mdi-file-image",
    "js": "mdi-language-javascript",
    "md": "mdi-language-markdown",
    "ods": "mdi-file-table",
    "odt": "mdi-file-document-outline",
    "ots": "mdi-file-table",
    "ott": "mdi-file-document-outline",
    "pdf": "mdi-file-document-outline",
    "php": "mdi-language-php",
    "png": "mdi-file-image",
    "py": "mdi-language-python",
    "rtf": "mdi-file-document-outline",
    "ts": "mdi-language-typescript",
    "txt": "mdi-file-document-outline",
    "xls": "mdi-file-table",
    "xlsm": "mdi-file-table",
    "xlsx": "mdi-file-table",
    "xltm": "mdi-file-table",
    "xltx": "mdi-file-table",
  };

  const DISPLAY_MODE_INFO = "info";
  const DISPLAY_MODE_OWN_FILES = "own";
  const DISPLAY_MODE_SHARED_FILES = "shared";
  const OBJECT_TYPE_FILE = "file";
  const OBJECT_TYPE_DIRECTORY = "directory";
  const ACTION_CREATE_DIRECTORY = 0;
  const ACTION_DELETE_DIRECTORY = 1;
  const ACTION_DELETE_FILE = 2;
  const ACTION_DOWNLOAD_FILE = 3;
  const ACTION_MOVE_DIRECTORY = 4;
  const ACTION_MOVE_FILE = 5;
  const ACTION_RENAME_DIRECTORY = 6;
  const ACTION_RENAME_FILE = 7;
  const ACTION_SHARE_DIRECTORY = 8;
  const ACTION_SHARE_FILE = 9;
  const ACTION_UPLOAD_FILE = 10;
  const DEFAULT_FILE_ACTIONS = Object.freeze([
    ACTION_DELETE_FILE,
    ACTION_DOWNLOAD_FILE,
    ACTION_MOVE_FILE,
    ACTION_RENAME_FILE,
    ACTION_SHARE_FILE
  ]);
  const DEFAULT_DIRECTORY_ACTIONS = Object.freeze([
    ACTION_CREATE_DIRECTORY,
    ACTION_DELETE_DIRECTORY,
    ACTION_MOVE_DIRECTORY,
    ACTION_RENAME_DIRECTORY,
    ACTION_SHARE_DIRECTORY,
    ACTION_UPLOAD_FILE
  ]);

  let nextSpecialID = 0;
  let activeDisplayMode = null;

  let snackbar = null;
  
  function displayMessage(data, extra=null) {
    if(data.message !== undefined)
      console.log(data.message);
    if(extra != null) {
      if(typeof(extra) === "object" && extra instanceof Error) {
        console.log(extra);
      } else {
        try {
          console.log(JSON.stringify(extra));
        } catch {
          console.log(extra);
        }
      }
    }
    if(snackbar == null)
      return;
    let suffix = null;
    if(extra != null) {
      if(Object.prototype.hasOwnProperty.call(extra, "message")) {
        suffix = extra.message;
      } else if(Object.prototype.hasOwnProperty.call(extra, "msg")) {
        suffix = extra.msg;
      } else if(Object.prototype.hasOwnProperty.call(extra, "status")) {
        suffix = extra.status;
      } else if(typeof(extra) === "string") {
        suffix = extra;
      } else {
        try {
          suffix = JSON.stringify(extra);
        } catch {
          suffix = null;
        }
      }
    }
    if(data.userMessage != null) {
      data.message = data.userMessage;
      suffix = null;
    }
    if(suffix != null) {
      if(data.message === undefined)
        data.message = suffix;
      else
        data.message += ": " + suffix;
    }
    if(data.message !== undefined)
      snackbar.show(data);
  }

  function getNextSpecialID(name) {
    return name == null ? "special/object" + nextSpecialID++ : "special/named/" + name;
  }

  function findIcon(isDir, entry) {
    if(isDir)
      return "mdi-folder"
    const extension = entry.name.replace(/^(?:.*\.)?([^.]+)$/, "$1").toLowerCase();
    return Object.prototype.hasOwnProperty.call(FILE_ICONS, extension) ?
      FILE_ICONS[extension] :
      FILE_ICONS[""];
  }

  function createInfoNode(message) {
    return {
      id: getNextSpecialID(),
      name: message,
      disabled: true,
      displayMode: DISPLAY_MODE_INFO
    };
  }

  function sortChildNodes(a, b) {
    if(!Object.prototype.hasOwnProperty.call(a, "object")) {
      if(Object.prototype.hasOwnProperty.call(b, "object"))
        return -1;
    } else if(!Object.prototype.hasOwnProperty.call(b, "object")) {
      return 1;
    }
    if(a.object.type === OBJECT_TYPE_DIRECTORY) {
      if(b.object.type !== OBJECT_TYPE_DIRECTORY)
        return -1;
    } else if(b.object.type === OBJECT_TYPE_DIRECTORY) {
      return 1;
    }
    return String.prototype.localeCompare.call(a.name.toLowerCase(), b.name.toLowerCase());
  }

  function parseChildren(displayMode, children) {
    return children.map(c => {
      const isDir = c.type === "directory";
      const e = isDir ? c.directory : c.file;
      return {
        id: (isDir ? OBJECT_TYPE_DIRECTORY : OBJECT_TYPE_FILE) + "/" + e.id,
        name: e.name,
        displayIcon: findIcon(isDir, e),
        owner: e.owner.displayName,
        displayMode: displayMode,
        object: {
          type: isDir ? OBJECT_TYPE_DIRECTORY : OBJECT_TYPE_FILE,
          id: e.id,
          permittedActions: isDir ? DEFAULT_DIRECTORY_ACTIONS : DEFAULT_FILE_ACTIONS
        },
        ...(isDir ? {children: []} : {})
      };
    });
  }

  async function loadChildrenToNode(node, ...childPromises) {
    node.children.push(...(await Promise.all(childPromises))
      .flat(1)
      .sort(sortChildNodes)
      .map(child => {
        child["parentNode"] = node;
        return child;
      }));
    if(node.children.length === 0)
      node.children.push(createInfoNode("Dieses Verzeichnis ist leer"));
    return Promise.resolve(node);
  }

  async function loadDirectoryChildrenToNode(node, directoryID) {
    return loadChildrenToNode(node, fileservice.getDirectory(directoryID)
        .then(directoryResponse => parseChildren(node.displayMode, directoryResponse.directory.children)))
        .catch(err => {
          displayMessage({message: "Fehler beim Abrufen des Verzeichnisinhalts"}, err);
          return loadChildrenToNode(node, Promise.resolve([createInfoNode("Verzeichnisinhalt konnte nicht abgerufen werden")]));
        });
  }

  export default {
    name: 'MainView',
    components: {
      ActionDialog,
      MainNavigationBar,
      ManageContactsDialog,
      ManageSharesDialog,
      SnackbarHelper
    },
    beforeRouteEnter(to, _from, next) {
      if(!session.isLoggedIn()) {
        next({name: "login"});
        return;
      }
      next();
    },
    created() {
      this.displayMessage = displayMessage;
      this.CONST = Object.freeze({
        DISPLAY_MODE_INFO: DISPLAY_MODE_INFO,
        DISPLAY_MODE_OWN_FILES: DISPLAY_MODE_OWN_FILES,
        DISPLAY_MODE_SHARED_FILES: DISPLAY_MODE_SHARED_FILES,
        OBJECT_TYPE_FILE: OBJECT_TYPE_FILE,
        OBJECT_TYPE_DIRECTORY: OBJECT_TYPE_DIRECTORY,
        ACTION_CREATE_DIRECTORY: ACTION_CREATE_DIRECTORY,
        ACTION_DELETE_DIRECTORY: ACTION_DELETE_DIRECTORY,
        ACTION_DELETE_FILE: ACTION_DELETE_FILE,
        ACTION_DOWNLOAD_FILE: ACTION_DOWNLOAD_FILE,
        ACTION_MOVE_DIRECTORY: ACTION_MOVE_DIRECTORY,
        ACTION_MOVE_FILE: ACTION_MOVE_FILE,
        ACTION_RENAME_DIRECTORY: ACTION_RENAME_DIRECTORY,
        ACTION_RENAME_FILE: ACTION_RENAME_FILE,
        ACTION_SHARE_DIRECTORY: ACTION_SHARE_DIRECTORY,
        ACTION_SHARE_FILE: ACTION_SHARE_FILE,
        ACTION_UPLOAD_FILE: ACTION_UPLOAD_FILE
      });
      this.$watch(() => this.$route.params, () => this.initialize(), {immediate: true});
    },
    mounted() {
      snackbar = this.$refs.snackbar;
      this.dialogs.confirmation.dialog = this.$refs.confirmationDialog;
      this.dialogs.confirmDeleteDirectory.dialog = this.$refs.confirmationDialogDeleteDirectory;
      this.dialogs.uploadFileDialog.dialog = this.$refs.uploadFileDialog;
      this.dialogs.createDirectoryDialog.dialog = this.$refs.createDirectoryDialog;
      this.dialogs.createShareDialog.dialog = this.$refs.createShareDialog;
      this.dialogs.renameDialog.dialog = this.$refs.renameDialog;
      this.dialogs.moveDialog.dialog = this.$refs.moveDialog;
    },
    data: () => ({
      selectedDisplayModeID: 0,
      displayedListEntries: [],
      displayedListEntriesOpen: [],
      displayedListEntriesOpenChanged: false,
      dialogs: {
        confirmation: {
          dialog: null
        },
        confirmDeleteDirectory: {
          dialog: null,
          cascade: false
        },
        uploadFileDialog: {
          dialog: null,
          selectedFiles: []
        },
        createDirectoryDialog: {
          dialog: null,
          directoryName: ""
        },
        createShareDialog: {
          dialog: null,
          targetsDirectory: false,
          contactsByName: null,
          selectedContactName: null,
          writePermission: false
        },
        renameDialog: {
          dialog: null,
          newName: ""
        },
        moveDialog: {
          dialog: null,
          options: {},
          seletectedTarget: ""
        }
      }
    }),
    computed: {},
    methods: {
      initialize() {
        this.setActiveView(DISPLAY_MODE_OWN_FILES, true);
      },
      setActiveView(displayMode, force=false) {

        if(activeDisplayMode === displayMode && !force)
          return;
        activeDisplayMode = displayMode;

        const rootID = getNextSpecialID(displayMode + "-root");
        let name = "/";
        if(displayMode === DISPLAY_MODE_OWN_FILES)
          name = "Eigene Dateien";
        else if(displayMode === DISPLAY_MODE_SHARED_FILES)
          name = "Mit mir geteilte Dateien";

        this.displayedListEntries = [
          {
            id: rootID,
            name: name,
            displayMode: displayMode,
            object: {
              type: OBJECT_TYPE_DIRECTORY,
              id: null,
              permittedActions: []
            },
            children: []
          }
        ];

        this.ensureTreeOpenEntriesSync();
        this.displayedListEntriesOpen = [];
        setImmediate(() => {
          // Return control before writing again to ensure that Vue sees
          // the empty array
          if(!this.displayedListEntriesOpen.includes(rootID))
            this.displayedListEntriesOpen.push(rootID);
          this.displayedListEntriesOpenChanged = true;
        });

      },
      triggerAction(action, params) {
        switch(action) {
        case ACTION_CREATE_DIRECTORY: {
          fileservice.createDirectory(params.targetNode.object.id, this.dialogs.createDirectoryDialog.directoryName)
            .then((() => this.refreshNode(params.targetNode)).bind(this))
            .catch(err => displayMessage({message: "Failed to create directory \"" + this.dialogs.createDirectoryDialog.directoryName + "\""}, err));
          return;
        }
        case ACTION_DELETE_DIRECTORY: {
          fileservice.deleteDirectory(params.targetNode.object.id, this.dialogs.confirmDeleteDirectory.cascade)
            .then((() => this.refreshNode(params.targetNode.parentNode)).bind(this))
            .catch(err => {
              if(err.body != null && err.body.status === "not_empty")
                displayMessage({message: "Failed to delete directory \"" + params.targetNode.name + "\"", userMessage: "Das Verzeichnis ist nicht leer."}, err);
              else if(err.body != null && err.body.status === "permission_denied")
                displayMessage({message: "Failed to delete directory \"" + params.targetNode.name + "\"", userMessage: "Sie sind nicht berechtigt, dieses Verzeichnis zu löschen."}, err)
              else
                displayMessage({message: "Failed to delete directory \"" + params.targetNode.name + "\""}, err);
            });
          return;
        }
        case ACTION_DELETE_FILE: {
          fileservice.deleteFile(params.targetNode.object.id)
            .then((() => this.refreshNode(params.targetNode.parentNode)).bind(this))
            .catch(err => {
              if(err.body != null && err.body.status === "permission_denied")
                displayMessage({message: "Failed to delete file \"" + params.targetNode.name + "\"", userMessage: "Sie sind nicht berechtigt, diese Datei zu löschen."}, err)
              else
                displayMessage({message: "Failed to delete file \"" + params.targetNode.name + "\""}, err)
            });
          return;
        }
        case ACTION_DOWNLOAD_FILE: {
          fileservice.downloadFile(params.targetNode.object.id, params.targetNode.name)
            .catch(err => displayMessage({message: "Failed to download file \"" + params.targetNode.name + "\""}, err));
          return;
        }
        case ACTION_MOVE_DIRECTORY: {
          const targetNode = this.dialogs.moveDialog.options[this.dialogs.moveDialog.seletectedTarget];
          fileservice.moveDirectory(params.targetNode.object.id, targetNode.object.id)
            .then((() => this.refreshNode(params.targetNode.parentNode)).bind(this))
            .then((() => this.refreshNode(targetNode)).bind(this))
            .catch(err => displayMessage({message: "Failed to move directory \"" + params.targetNode.name + "\""}, err));
          return;
        }
        case ACTION_MOVE_FILE: {
          const targetNode = this.dialogs.moveDialog.options[this.dialogs.moveDialog.seletectedTarget];
          fileservice.moveFile(params.targetNode.object.id, targetNode.object.id)
            .then((() => this.refreshNode(params.targetNode.parentNode)).bind(this))
            .then((() => this.refreshNode(targetNode)).bind(this))
            .catch(err => displayMessage({message: "Failed to move file \"" + params.targetNode.name + "\""}, err));
          return;
        }
        case ACTION_RENAME_DIRECTORY: {
          fileservice.renameDirectory(params.targetNode.object.id, this.dialogs.renameDialog.newName)
            .then((() => this.refreshNode(params.targetNode.parentNode)).bind(this))
            .catch(err => displayMessage({message: "Failed to rename directory \"" + params.targetNode.name + "\""}, err));
          return;
        }
        case ACTION_RENAME_FILE: {
          fileservice.renameFile(params.targetNode.object.id, this.dialogs.renameDialog.newName)
            .then((() => this.refreshNode(params.targetNode.parentNode)).bind(this))
            .catch(err => displayMessage({message: "Failed to rename file \"" + params.targetNode.name + "\""}, err));
          return;
        }
        case ACTION_SHARE_DIRECTORY: {
          const selectedContactName = this.dialogs.createShareDialog.selectedContactName;
          if(selectedContactName == null) {
            displayMessage({userMessage: "Bitte wählen Sie einen Kontakt aus."});
            return;
          }
          const subjectID = this.dialogs.createShareDialog.contactsByName[selectedContactName];
          if(subjectID == null) {
            displayMessage({userMessage: "Bitte wählen Sie einen Kontakt aus."});
            return;
          }
          fileservice.createShare("directory", params.targetNode.object.id, subjectID, this.dialogs.createShareDialog.writePermission)
            .then(() => displayMessage({userMessage: "Verzeichnis freigegeben.", icon: "mdi-information", color: "green"}))
            .catch(err => displayMessage({message: "Failed to share directory \"" + params.targetNode.name + "\""}, err));
          return;
        }
        case ACTION_SHARE_FILE: {
          const selectedContactName = this.dialogs.createShareDialog.selectedContactName;
          if(selectedContactName == null) {
            displayMessage({userMessage: "Bitte wählen Sie einen Kontakt aus."});
            return;
          }
          const subjectID = this.dialogs.createShareDialog.contactsByName[selectedContactName];
          if(subjectID == null) {
            displayMessage({userMessage: "Bitte wählen Sie einen Kontakt aus."});
            return;
          }
          fileservice.createShare("file", params.targetNode.object.id, subjectID, this.dialogs.createShareDialog.writePermission)
            .then(() => displayMessage({userMessage: "Datei freigegeben.", icon: "mdi-information", color: "green"}))
            .catch(err => displayMessage({message: "Failed to share file \"" + params.targetNode.name + "\""}, err));
          return;
        }
        case ACTION_UPLOAD_FILE: {
          const files = this.dialogs.uploadFileDialog.selectedFiles;
          Promise.all(files.map(f => {
              return readFileToBlob(f)
                .then(blob => fileservice.uploadFile(blob, f.name, params.targetNode.object.id))
                .catch(err => {
                  if(err.body != null && err.body.status === "duplicate_name")
                    displayMessage({message: "Failed to upload file \"" + f.name + "\"", userMessage: "Eine Datei mit dem Namen \"" + f.name + "\" existiert bereits."}, err);
                  else
                    displayMessage({message: "Failed to upload file \"" + f.name + "\""}, err);
                  throw err;
                });
            }))
            .then(() => displayMessage({userMessage: "Hochladen erfolgreich", icon: "mdi-information", color: "green"}))
            .catch(err => displayMessage({message: "File upload failed", userMessage: "Das Hochladen konnte nicht erfolgreich abgeschlossen werden."}, err))
            .then((() => this.refreshNode(params.targetNode)).bind(this));
          return;
        }
        default:
          console.log("Bad action: " + action);
          return;
        }
      },
      calculateMoveTargets() {
        let options = [];
        let stack = [...this.displayedListEntries];
        while(stack.length > 0) {
          const next = stack.pop();
          if(next.object == null || next.object.type !== OBJECT_TYPE_DIRECTORY)
            continue;
          let text = "";
          let n = next;
          while(n != null) {
            text = n.name + "/" + text;
            n = n.parentNode;
          }
          options[text] = next;
          if(next.children != null)
            stack.push(...[...next.children].reverse())
        }
        return options;
      },
      prepareShareDialog() {
        (async () => {
            const userinfo = (await fileservice.getUserInfo()).userinfo;
            return userinfo.contacts.map(c => ({id: c.id, name: c.displayName}));
          })()
          .then((contacts => {
            const contactsByName = {};
            for(let c of contacts)
              contactsByName[c.name] = c.id;
            this.dialogs.createShareDialog.contactsByName = contactsByName;
          }).bind(this))
          .catch(err => displayMessage({message: 'Failed to load contacts'}, err));
        this.dialogs.createDirectoryDialog.contactsByName = null;
        this.dialogs.createShareDialog.selectedContactName = null;
      },
      ensureTreeOpenEntriesSync() {
        // Ensures that the array of opened nodes is up to date
        // by fiering the corresponding event manually, if these
        // entries have been changed
        if(this.displayedListEntriesOpenChanged) {
          try {
            this.$refs.fileTree.emitOpen();
          } catch(err) {
            console.log("Failed to force tree sync")
            console.log(err);
          }
          this.displayedListEntriesOpenChanged = false;
        }
      },
      async loadEntries(parent) {

        if(!Object.prototype.hasOwnProperty.call(parent, "object") ||  parent.object.type !== OBJECT_TYPE_DIRECTORY)
          return Promise.resolve(parent);
        
        if(parent.displayMode === DISPLAY_MODE_OWN_FILES) {
          if(parent.object.id == null) {
            // Root node of the own files
            try {
              const userinfo = await fileservice.getUserInfo();
              parent.object.id = userinfo.userinfo.personalRootDirectory;
              // Once the ID is known, children can be added ba the user
              for(let action of [ACTION_CREATE_DIRECTORY, ACTION_SHARE_DIRECTORY, ACTION_UPLOAD_FILE])
                if(!parent.object.permittedActions.includes(action))
                  parent.object.permittedActions.push(action);
            } catch(err) {
              displayMessage({message: "Fehler beim Abrufen der Benutzerinformationen"}, err);
              return loadChildrenToNode(parent, Promise.resolve([createInfoNode("Verzeichnisinhalt konnte nicht abgerufen werden")]));
            }
          }
          return loadDirectoryChildrenToNode(parent, parent.object.id);
        } else if(parent.displayMode === DISPLAY_MODE_SHARED_FILES) {
          if(parent.object.id == null) {
            // Root node of the shared files
            let shares;
            try {
              const userinfo = await fileservice.getUserInfo();
              shares = userinfo.userinfo.receivedShares;
            } catch(err) {
              displayMessage({message: "Fehler beim Abrufen der Benutzerinformationen"}, err);
              return loadChildrenToNode(parent, Promise.resolve([createInfoNode("Verzeichnisinhalt konnte nicht abgerufen werden")]));
            }
            const childPromises = shares.map(share => {
              return fileservice.getShare(share.id)
                .then(shareResponse => parseChildren(parent.displayMode, [shareResponse.share.target]))
                .catch((err) => {
                  console.log("Failed to get share " + share.id + ": " + JSON.stringify(err));
                  return Promise.resolve([]);
                });
            });
            return loadChildrenToNode(parent, ...childPromises);
          } else {
            return loadDirectoryChildrenToNode(parent, parent.object.id);
          }
        } else if(parent.displayMode === DISPLAY_MODE_INFO) {
          return Promise.resolve(parent);
        } else {
          console.error("Got invalid display mode: " + parent.displayMode);
          return Promise.resolve(parent);
        }

      },
      async refreshNode(node) {

        if(node.children == null)
          return;
        const nodeList = Object.prototype.hasOwnProperty.call(node, "parentNode") ?
          node.parentNode.children :
          this.displayedListEntries;
        let index = nodeList.indexOf(node);
        if(index < 0)
          return;
        
        nodeList.splice(index, 1);
        node.children = [];
        this.ensureTreeOpenEntriesSync();
        index = this.displayedListEntriesOpen.indexOf(node.id);
        const wasOpen = index >= 0;
        if(wasOpen)
          this.displayedListEntriesOpen.splice(index, 1);
        
        setImmediate(() => {
          // Return control before writing again to ensure that Vue sees
          // the empty array
          nodeList.push(node);
          nodeList.sort(sortChildNodes);
          if(wasOpen) {
            setImmediate(() => this.displayedListEntriesOpen.push(node.id));
            this.displayedListEntriesOpenChanged = true;
          }
        });

      }
    }
  }
</script>
