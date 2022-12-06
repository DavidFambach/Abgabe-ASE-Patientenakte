
<template>
  <v-app>
    <custom-app-bar />

    <v-main class="grey lighten-3">
        <v-row>
          <v-col cols="2">
            <v-sheet >
              <v-list color="transparent">
                  <v-list-item-group
                  v-model="selectedDisplayModeID"
                  background-color="secondary"
                  >
                <v-list-item v-on:click="haneleClickOwnFiles">
                  <v-list-item-content>
                    <v-list-item-title>
                      Eigene Dateien
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item v-on:click="haneleClickSharedFiles">
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
              open-on-click hoverable dense>
              <template v-slot:label="{ item }">
                <v-row justify="space-between">
                  <v-col>{{ item.name }}</v-col>
                  <v-col v-if="'owner' in item" class="text-right pr-10">{{ item.owner }}</v-col>
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

        <snackbar-helper ref="snackbar" />

    </v-main>
  </v-app>
</template>

<script>
  import CustomAppBar from '@/components/CustomAppBar.vue'
  import SnackbarHelper from '../components/SnackbarHelper.vue';
  import { setOwnUserID, setOwnToken, getUserInfo, getDirectory, getShare } from "@/fileservice"
  
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
    "pdf": "mdi-file-pdf",
    "php": "mdi-language-php",
    "png": "mdi-file-image",
    "py": "mdi-language-python",
    "ts": "mdi-language-typescript",
    "txt": "mdi-file-document-outline",
    "xls": "mdi-file-table",
    "xlsm": "mdi-file-table",
    "xlsx": "mdi-file-table",
    "xltm": "mdi-file-table",
    "xltx": "mdi-file-table",
  }

  const DISPLAY_MODE_INFO = "info";
  const DISPLAY_MODE_OWN_FILES = "own";
  const DISPLAY_MODE_SHARED_FILES = "shared";
  const OBJECT_TYPE_FILE = "file";
  const OBJECT_TYPE_DIRECTORY = "directory";

  let nextSpecialID = 0;
  let activeDisplayMode = null;

  let snackbar = null;
  
  function displayMessage(data, extra) {
    let suffix = null;
    if(extra != null) {
      if(Object.prototype.hasOwnProperty.call(extra, "message"))
        suffix = extra.message;
      else if(Object.prototype.hasOwnProperty.call(extra, "msg"))
        suffix = extra.msg;
      else if(Object.prototype.hasOwnProperty.call(extra, "status"))
        suffix = extra.status;
      else if(typeof(extra) === "string")
        suffix = extra;
      else
        suffix = JSON.stringify(extra);
    }
    if(suffix != null)
      data.message += ": " + suffix;
    if(snackbar == null)
      console.log(data.message);
    else
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
          id: e.id
        },
        ...(isDir ? {children: []} : {})
      };
    });
  }

  async function loadChildrenToNode(node, ...childPromises) {
    node.children.push(...(await Promise.all(childPromises))
      .flat(1).sort((a, b) => {
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
      }));
    if(node.children.length === 0)
      node.children.push(createInfoNode("Dieses Verzeichnis ist leer"));
    return Promise.resolve(node);
  }

  async function loadDirectoryChildrenToNode(node, directoryID) {
    return loadChildrenToNode(node, getDirectory(directoryID)
        .then(directoryResponse => parseChildren(node.displayMode, directoryResponse.directory.children)))
        .catch(err => {
          console.log("Failed to get directory " + directoryID + ": " + JSON.stringify(err));
          displayMessage({message: "Fehler beim Abrufen des Verzeichnisinhalts"}, err);
          loadChildrenToNode(node, Promise.resolve([createInfoNode("Verzeichnisinhalt konnte nicht abgerufen werden")]));
          return Promise.resolve(node);
        });
  }

  export default {
    name: 'AboutView',
    components: {
      CustomAppBar,
      SnackbarHelper
    },
    created() {},
    mounted() {
      snackbar = this.$refs.snackbar;
      this.setActiveView(DISPLAY_MODE_OWN_FILES);
    },
    data: () => ({
      selectedDisplayModeID: 0,
      displayedListEntries: [],
      displayedListEntriesOpen: []
    }),
    computed: {},
    methods: {
      haneleClickOwnFiles() {
        this.setActiveView(DISPLAY_MODE_OWN_FILES);
      },
      haneleClickSharedFiles() {
        this.setActiveView(DISPLAY_MODE_SHARED_FILES);
      },
      setActiveView(displayMode) {

        if(activeDisplayMode === displayMode)
          return;
        activeDisplayMode = displayMode;

        const rootID = getNextSpecialID(displayMode + "-root");
        this.displayedListEntries = [
          {
            id: rootID,
            name: "/",
            displayMode: displayMode,
            object: {type: OBJECT_TYPE_DIRECTORY, id: null},
            children: []
          }
        ];
        this.displayedListEntriesOpen = [];
        setImmediate(() => {
          // Return control before writing again to ensure that Vue sees
          // the empty array
          if(!this.displayedListEntriesOpen.includes(rootID))
            this.displayedListEntriesOpen.push(rootID);
        });

      },
      async loadEntries(parent) {

        if(!Object.prototype.hasOwnProperty.call(parent, "object") ||  parent.object.type !== OBJECT_TYPE_DIRECTORY)
          return Promise.resolve(parent);
        
        if(parent.displayMode === DISPLAY_MODE_OWN_FILES) {
          let directoryID;
          if(parent.object.id == null) {
            // Root node of the own files
            try {
              const userinfo = await getUserInfo();
              directoryID = userinfo.userinfo.personalRootDirectory;
            } catch(err) {
              console.log("Failed to get user information: " + JSON.stringify(err));
              displayMessage({message: "Fehler beim Abrufen der Benutzerinformationen"}, err);
              return loadChildrenToNode(parent, Promise.resolve([createInfoNode("Verzeichnisinhalt konnte nicht abgerufen werden")]));
            }
          } else {
            directoryID = parent.object.id;
          }
          return loadDirectoryChildrenToNode(parent, directoryID);
        } else if(parent.displayMode === DISPLAY_MODE_SHARED_FILES) {
          if(parent.object.id == null) {
            // Root node of the shared files
            let shares;
            try {
              const userinfo = await getUserInfo();
              shares = userinfo.userinfo.receivedShares;
            } catch(err) {
              console.log("Failed to get user information: " + JSON.stringify(err));
              displayMessage({message: "Fehler beim Abrufen der Benutzerinformationen"}, err);
              return loadChildrenToNode(parent, Promise.resolve([createInfoNode("Verzeichnisinhalt konnte nicht abgerufen werden")]));
            }
            const childPromises = shares.map(share => {
              return getShare(share.id)
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

      }
    }
  }
</script>


