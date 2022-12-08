
<template>
    <v-app-bar
      app
      color="primary"
      flat
    >
        <!-- Icon -->
        <v-img
          alt="Logo"
          class="shrink mr-2"
          contain
          src="https://cdn-icons-png.flaticon.com/512/55/55025.png"
          transition="scale-transition"
          width="40"
        />
        <v-btn depressed href="./">Dateiansicht</v-btn>


        <!-- Geteilt Liste. Button und Dialog -->
        <div class="text-center">
          <v-btn depressed v-on:click.stop="openShareDialog()">
            Aktive Freigaben
          </v-btn>
        </div>


        <!-- Arzt hinzufügen. Button und Dialog -->
        <div class="text-center">
          <v-btn depressed v-on:click.stop="openContactsDialog()">
            Kontakte verwalten
          </v-btn>
        </div>
        

        <v-spacer></v-spacer>

        <!-- Avatar oben rechts -->
        <v-menu
              bottom
              min-width="200px"
              rounded
              offset-y
            >
              <template v-slot:activator="{ on }">
                <v-btn
                  icon
                  x-large
                  v-on="on"
                >
                  <v-avatar
                    color="brown"
                    size="48"
                  >
                    <span class="white--text text-h5">{{ user.initialien }}</span>
                  </v-avatar>
                </v-btn>
              </template>
              <!-- Dialog für Avatar -->
              <v-card>
                <v-list-item-content class="justify-center">
                  <div class="mx-auto text-center">
                    <v-avatar
                      color="brown"
                    >
                      <span class="white--text text-h5">{{ user.initialien }}</span>
                    </v-avatar>
                    <h3>{{ user.name }}</h3>
                    <p class="text-caption mt-1">
                      {{ user.email }}
                    </p>
                    <p class="text-caption mt-1">
                      {{ user.benutzerid }}
                    </p>
                    <v-divider class="my-3"></v-divider>
                    <!-- Passwort ändern. Knopf und Dialog -->
                    <div class="text-center">
                      <v-dialog
                        v-model="dialogPW"
                        width="1000"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn
                            depressed
                            
                            text
                            v-bind="attrs"
                            v-on="on"
                          >
                            Passwort ändern
                          </v-btn>
                        </template>

                        <v-card>
                          <v-card-title class="text-h5 grey lighten-2">
                            Passwort ändern
                          </v-card-title>
                          <v-card-text>
                          <v-container>
                          <v-text-field
                              v-model="Passwort"
                              :value="Passwort"
                              name="Passwort"
                              label="Passwort"
                              placeholder="Passwort"
                              required
                              color="light grey"
                              :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
                                @click:append="() => (value = !value)"
                                :type="value ? 'password' : 'text'"
                                :rules="[rules.password]"
                                @input="_=>userPassword=_" 
                          ></v-text-field>
                          </v-container>
                          </v-card-text>
                          <v-divider></v-divider>
                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                              color="secondary"
                              text
                              @click="dialogPW = false"
                            >
                            Akzeptieren
                            </v-btn>
                            <v-btn
                              color="secondary"
                              text
                              @click="dialogPW = false"
                            >
                              Schließen
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                    </div>

                    <!-- Knopf zum Ausloggen -->
                    <v-divider class="my-3"></v-divider>
                    <v-btn
                      depressed
                      
                      text
                      href="./Anmeldung"
                    >
                      Ausloggen
                    </v-btn>
                    
                  </div>
                </v-list-item-content>
              </v-card>
            </v-menu>
       
      
      
    </v-app-bar>
</template>

<script>
  export default {
    props: {
        openContactsDialog: Function,
        openShareDialog: Function
    },
    data: () => ({
        dialogListe: false,
        dialogPW: false,
        dialogHochladen: false,
        dialogArzt: false,
        Passwort: "",
        valid:true,
       value:true,
       rules: {
        required: value => !!value || "Benötigt.",
        password: value => {
          const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})/;
          return (
            pattern.test(value) ||
            "Min. 8 Zeichen mit mindestens einem Groß- und Kleinbuchstaben, einer Nummer und einem Zeichen."
          );
        }
      }, 
      user: {
        name: 'Jonas Grohe',
        initialien: 'JG',
        email:'test@example.com',
        benutzerid:"#123456789",
      },
      ärzte: [
          {
            name: 'Arzt 1',
            test: 'test',
          },
          {
            name: 'Arzt 2',
            test: 'test',
          },
        ],
    }),
  }
</script>


