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
                             <v-text-field  v-if="isRegister"
                               v-model="Benutzername"
                               name="Benutzername"
                               label="Benutzername"
                               type="text"
                               placeholder="Benutzername"
                               required
                               color="light grey"
                               :rules="rules.required"
                            ></v-text-field>

                            <v-text-field
                               v-model="Email"
                               name="Email"
                               label="Email"
                               type="email"
                               placeholder="Email"
                               required
                               color="light grey"
                               :rules="(emailRules,rules.required)"
                               
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
                                 :rules="(rules.password,rules.required)"
                                 @input="_=>userPassword=_" 
                            ></v-text-field>
 
                            <v-text-field v-if="isRegister"
                               v-model="PasswortBestätigen"
                               name="PasswortBestätigen"
                               label="Passwort bestätigen"
                               type="password"
                               placeholder="Passwort bestätigen"
                               required
                               :rules="rules.required"
                               color="light grey"
                            ></v-text-field>
                            <div class="blue--text" v-if="isMailsent">
                              Der Benutzer wurde erfolgreich registriert. Bitte überprüfen Sie Ihre E-Mail und bestätigen Sie die Registrierung durch Klicken auf den Link in der E-Mail.
                            </div>

                            <div class="red--text"> {{errorMessage}}</div>

                            <v-btn type="submit" class="mt-4" color="light grey"> {{isRegister ? "Registrieren" :" Anmelden"}} </v-btn>
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
       Email: "",
       PasswortBestätigen: "",
       emailRules: "",
       isRegister : false,
       isMailsent: false,
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
            var myHeaders = new Headers();
            myHeaders.append("Content-Type", "application/json");
            myHeaders.append("Accept", "application/json");
            
            var raw = JSON.stringify({
            "email": this.Email,
            "password": this.Passwort
            });
            console.log(raw)

            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
            };

            fetch("http://127.0.0.1/auth/login/", requestOptions)
            .then(response => {
               if(response.status>=200 && response.status<300){
                  this.isRegister = false;
                  this.isMailsent = true;
               }
               else{
                  this.errorMessage="Es ist ein Fehler aufgetreten"
                  response.json().then((json)=>{
                     this.errorMessage = json.detail
                     console.log(json.detail)
                  })
                  
                  .catch(error => console.log(error));
               }
            })
            .catch(error => console.log(error));
        },

     register() {
        if(this.Passwort == this.PasswortBestätigen){
            var myHeaders = new Headers();
            myHeaders.append("Content-Type", "application/json");
            myHeaders.append("Accept", "application/json");
            
            var raw = JSON.stringify({
            "username": this.Benutzername,
            "email": this.Email,
            "password": this.Passwort,
            });

            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
            };

            fetch("http://127.0.0.1/auth/register/", requestOptions)
            // .then(response =>response.json())
            .then(response => {
               if(response.status>=200 && response.status<300){
                  this.isRegister = false;
                  this.isMailsent = true;
               }
               else{
                  this.errorMessage="Es ist ein Fehler aufgetreten"
                  response.json().then((json)=>{
                     this.errorMessage = json.error
                     console.log(json.error)
                  })
                  
                  .catch(error => console.log(error));
               }
            })
            .catch(error => console.log(error));
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