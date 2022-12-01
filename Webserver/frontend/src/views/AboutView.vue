
<template>
  <v-app>
    <custom-app-bar />

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      Eigene Dateien
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      Geteilte Dateien
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
              min-height="70vh"
              rounded="lg"
            >
              <!--  -->
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import CustomAppBar from '@/components/CustomAppBar.vue'

  export default {
    name: 'AboutView',
    components: {
      CustomAppBar,
    },
    data: () => ({
      links: [
        'Dateiansicht',
        'Neue Datei hochladen',
        'Arzt hinzufügen',
        'Arzt Liste',
      ],
      user: {
        name: 'Jonas Grohe',
        initials: 'JG',
        email:'test@example.com'
      },
      
    }),
  }
</script>


