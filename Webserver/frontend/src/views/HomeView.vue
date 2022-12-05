
<template>
  <v-app>
    <custom-app-bar />

    <v-main class="grey lighten-3">
        <v-row>
          <v-col cols="2">
            <v-sheet >
              <v-list color="transparent">
                  <v-list-item-group
                  v-model="selectedItem"
                  background-color="secondary"
                  >
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title v-on:click="ClickEigene">
                      Eigene Dateien
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title v-on:click="ClickGeteilt">
                      Geteilte Dateien
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
              height="80vh"
              width="95%"
              rounded="lg"
            >
            <v-simple-table v-if="!isGeteilt">
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        Dateiname
                      </th>
                      <th class="text-left">
                        Änderungsdatum
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="item in EigeneDateien"
                      :key="item.name"
                    >
                      <td width="80%">{{ item.name }}</td>
                      <td>{{ item.datum }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>

              <v-simple-table v-if="isGeteilt">
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        Dateiname
                      </th>
                      <th class="text-left">
                        Änderungsdatum
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="item in GeteilteDateien"
                      :key="item.name"
                    >
                      <td width="80%">{{ item.name }}</td>
                      <td>{{ item.datum }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>


            </v-sheet>
          </v-col>
        </v-row>
    </v-main>
  </v-app>
</template>

<script>
  import CustomAppBar from '@/components/CustomAppBar.vue'
  import { setOwnUserID, getUserInfo, getDirectory } from "@/fileservice"

  export default {
    name: 'AboutView',
    components: {
      CustomAppBar,
    },
    created() {
      this.requestFiles();
    },
    data: () => ({
      isGeteilt:false,
      selectedItem:0,
      EigeneDateien: [
          {
            name: 'EigeneDatei1',
            datum: "1.12.2022",
          },
          {
            name: 'EigeneDatei2',
            datum: "1.12.2022",
          },
        ],
        GeteilteDateien: [
          {
            name: 'GeteilteDatei1',
            datum: "1.12.2022",
          },
          {
            name: 'GeteilteDatei2',
            datum: "1.12.2022",
          },
        ],
    }),
    methods: {
      ClickGeteilt(){
        if(!this.isGeteilt){
          this.isGeteilt = true;}
      },
      ClickEigene(){
        if(this.isGeteilt){
          this.isGeteilt = false;}
      },
      requestFiles() {
        setOwnUserID(1);
        getUserInfo()
          .then(userinfo => getDirectory(userinfo.userinfo.personalRootDirectory))
          .then(directoryResponse => {
            const children = directoryResponse.directory.children
            this.EigeneDateien = children.map(c => {
              if(c.type === "directory")
                return {name: c.directory.name, datum: "01.01.1970"}
              else
                return {name: c.file.name, datum: "01.01.1970"}
            });
          })
          .catch(console.log);
      }
    }
  }
</script>


