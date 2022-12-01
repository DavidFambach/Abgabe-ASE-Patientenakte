<template>
    <v-app >
       <v-main>
          <v-container fluid fill-height>
             <v-layout align-center justify-center>
                <v-flex xs12 sm8 md4>
                   <v-card class="elevation-12">
                      <v-toolbar color="light grey">
                         <v-toolbar-title>{{isRegister ? "Registrierung" :" Anmeldung"}} </v-toolbar-title>
                      </v-toolbar>
                      <v-card-text>
                      <form ref="form" @submit.prevent="isRegister ? register() : login()">
                             <v-text-field
                               v-model="Benutzername"
                               name="Benutzername"
                               label="Benutzername"
                               type="text"
                               placeholder="Benutzername"
                               required
                               color="light grey"
                               :rules="rules.required"
                            ></v-text-field>

                            <v-text-field v-if="isRegister"
                               v-model="Email"
                               name="Email"
                               label="Email"
                               type="email"
                               placeholder="Email"
                               required
                               color="light grey"
                               :rules="(emailRules,rules.required)"
                               
                            ></v-text-field>

                            <v-text-field v-if="isRegister"
                               v-model="Vorname"
                               name="Vorname"
                               label="Vorname"
                               type="text"
                               placeholder="Vorname"
                               required
                               color="light grey"
                               :rules="rules.required"
                            ></v-text-field>

                            <v-text-field v-if="isRegister"
                               v-model="Nachname"
                               name="Nachname"
                               label="Nachname"
                               type="text"
                               placeholder="Nachname"
                               required
                               color="light grey"
                               :rules="rules.required"
                            ></v-text-field>

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
                                 :rules="[rules.password,rules.required]"
                                 @input="_=>userPassword=_" 
                            ></v-text-field>
 
                            <v-text-field v-if="isRegister"
                               v-model="Passwortbestätigen"
                               name="Passwort bestätigen"
                               label="Passwort bestätigen"
                               type="password"
                               placeholder="Passwort bestätigen"
                               required
                               :rules="rules.required"
                               color="light grey"
                            ></v-text-field>


                            <div class="red--text"> {{errorMessage}}</div>

                            <v-btn type="submit" class="mt-4" color="light grey" href="./"> {{isRegister ? "Registrieren" :" Anmelden"}} </v-btn>
                            <br>
                            <div class="grey--text mt-4">
                              oder
                            </div>

                            <v-btn class="mt-4" color="light grey" v-on:click="isRegister = !isRegister;"> {{isRegister ? "Mit bestehendem Benutzer anmelden" :" Neuen Benutzer registrieren"}} </v-btn>
                            <br>
                            <v-btn class="mt-4" color="light grey"> Mit Google Anmelden</v-btn>
                       </form>
                      </v-card-text>
                   </v-card>
                 
                </v-flex>
             </v-layout>
          </v-container>
       </v-main>
    </v-app>
 </template>
 
 <script>
 export default {
   name: "App",
   data() {
     return {
       Benutzername: "",
       Passwort: "",
       confirmPasswort: "",
       isRegister : false,
       errorMessage: "",
       valid:true,
       value:true,
       rules: {
        required:[ value => !!value || "Benötigt.",
        value => (value && value.length >= 1) || 'Benötigt',],
        password: value => {
          const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})/;
          return (
            pattern.test(value) ||
            "Min. 8 Zeichen mit mindestens einem Groß- und Kleinbuchstaben, einer Nummer und einem Zeichen."
          );
        }
      } 
     };
   },
   methods: {
     login() {
       const { Benutzername } = this;
       console.log(Benutzername + "logged in")
     },
     register() {
        if(this.Passwort == this.confirmPasswort){
           this.isRegister = false;
           this.errorMessage = "";
           this.$refs.form.reset();
        }
        else {
          this.errorMessage = "Passwort stimmt nicht überein";
        }
     }
   },
       computed: {
        toggleMessage : function() { 
           return this.isRegister ? this.stateObj.register.message : this.stateObj.login.message }
     }
 };
 </script>