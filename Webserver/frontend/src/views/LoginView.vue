<template>
	<v-app>
		<v-main>

			<v-container fluid fill-height>
				<v-layout align-center justify-center>
					<v-flex xs12 sm8 md6>
						<v-card class="elevation-12">
							<v-toolbar color="light grey">
								<v-toolbar-title>{{isRegister ? "Registrierung" :" Anmeldung"}}</v-toolbar-title>
							</v-toolbar>
							<v-card-text>
								<form class="d-flex flex-column" ref="form" @submit.prevent="isRegister ? register() : login()">

									<v-text-field ref="textfieldEMail" key="textfieldEMail"
										name="E-Mail-Adresse" label="E-Mail-Adresse" placeholder="E-Mail-Adresse"
										type="email" color="light grey"
										required v-model="user.email" :rules="[rules.notEmpty, rules.email]" />

									<v-text-field v-if="isRegister" key="textfieldTitle"
										name="Titel" label="Titel"
										placeholder="Titel" type="text" color="light grey"
										required v-model="user.title" />

									<v-text-field v-if="isRegister" key="textfieldFirstname"
										name="Vorname" label="Vorname"
										placeholder="Vorname" type="text" color="light grey"
										required v-model="user.firstname" :rules="[rules.notEmpty]" />

									<v-text-field v-if="isRegister" key="textfieldLastname"
										name="Nachname" label="Nachname"
										placeholder="Nachname" type="text" color="light grey"
										required v-model="user.lastname" :rules="[rules.notEmpty]" />

									<v-text-field ref="textfieldPassword" key="textfieldPassword"
										name="Passwort" label="Passwort"
										placeholder="Passwort" color="light grey"
										required v-model="password" :rules="[rules.notEmpty, rules.validPassword]"
										:type="showPassword ? 'text' : 'password'">
										<template v-slot:append>
											<v-btn icon tabindex="-1"
												v-on:click.stop="() => {showPassword = !showPassword}">
												<v-icon>{{showPassword ? "mdi-eye-off" : "mdi-eye"}}</v-icon>
											</v-btn>
										</template>
									</v-text-field>
									
									<v-text-field v-if="isRegister" key="textfieldRepeatPassword"
										name="Passwort bestätigen" label="Passwort bestätigen"
										placeholder="Passwort bestätigen" type="password" color="light grey"
										required v-model="passwordRepeated" :rules="[rules.notEmpty, rules.validPassword, rules.matchesPassword]" />

									<div class="red--text">{{errorMessage}}</div>

									<v-btn class="mt-4" color="light grey"
										v-on:click.stop="() => isRegister ? signUp() : logIn()">
										{{isRegister ? "Registrieren" :" Anmelden"}}
									</v-btn>
									
									<v-divider class="my-2" />

									<div class="d-flex flex-column">
										<v-btn color="light grey" v-on:click.stop="switchMode">
											{{isRegister ? "Mit bestehendem Benutzer anmelden" :" Neuen Benutzer registrieren"}}
										</v-btn>
										<v-btn class="mt-1" color="light grey" v-on:click.stop="logInWithGoogle">Mit Google Anmelden</v-btn>
									</div>
									
								</form>
							</v-card-text>
						</v-card>
					</v-flex>
				</v-layout>
			</v-container>

			<action-dialog ref="registrationSuccessfulDialog" />

		</v-main>
	</v-app>
</template>
 
<script>

	import ActionDialog from "@/components/ActionDialog.vue";
	import * as authservice from "@/authservice";
	import * as session from "@/session";

	export default {
		name: "LoginView",
		components: {
			ActionDialog
		},
		mounted() {
			this.dialogs.registrationSuccessfulDialog.dialog = this.$refs.registrationSuccessfulDialog;
			this.$refs.textfieldEMail.focus();
			this.checkActiveAuth();
		},
		data() {
			return {
				dialogs: {
					registrationSuccessfulDialog: {
						dialog: null
					}
				},
				password: "",
				passwordRepeated: "",
				showPassword: false,
				user: {
					title: "",
					firstname: "",
					lastname: "",
					email: ""
				},
				isRegister : false,
				errorMessage: "",
				rules: {
					notEmpty: value => value == null || value === "" ? "Dieses Feld ist erforderlich" : true,
					email: value => typeof(value) !== "string" || value.match(/^.+@.+\..+$/) == null ? "Bitte geben Sie eine gültige E-Mail-Adresse ein" : true,
					validPassword: value => typeof(value) !== "string" || value.match(/^.{10,}$/) == null ? "Das Passwort muss mindestens 10 Zeichen lang sein" : true,
					matchesPassword: value => value !== this.password ? "Die Passwörter stimmen nicht überein" : true
				}
			};
		},
		methods: {
			checkActiveAuth() {
				const googleOAuthCode = session.getExtraGoogleOAuthInfo();
				if(googleOAuthCode != null) {
					session.setExtraGoogleOAuthInfo(null);
					authservice.finalizeLogInWithGoogle(googleOAuthCode)
						.then(this.handleLoginResponse)
						.catch(err => {
							console.log(err);
							this.errorMessage = "Die Anmeldung mit Google ist fehlgeschlagen.";
						});
				}
			},
			switchMode() {
				if(this.isRegister) {
					this.isRegister = false;
					setImmediate((() => this.$refs.textfieldEMail.focus()).bind(this));
				} else {
					this.isRegister = true;
					setImmediate((() => this.$refs.textfieldEMail.focus()).bind(this));
				}
			},
			logIn() {
				authservice.logIn(this.user.email, this.password)
					.then(this.handleLoginResponse)
					.catch(err => {
						console.log("Failed to log in:");
						console.log(err);
						if(err.status === 401) {
							this.errorMessage = "Die E-Mail-Adresse oder das Passwort sind ungültig.";
							this.password = "";
							this.$refs.textfieldPassword.focus();
						} else {
							this.errorMessage = "Beim Anmeldeversuch ist ein Fehler aufgetreten.";
						}
					});
			},
			logInWithGoogle() {
				authservice.logInWithGoogle().then(console.log).catch(console.log);
				this.errorMessage = "Diese Operation wird noch nicht unterstützt.";
			},
			signUp() {
				if(this.user.email == null || this.user.email === ""
					|| this.user.firstname == null || this.user.firstname === ""
					|| this.user.lastname == null || this.user.lastname === ""
					|| this.password == null || this.password === "")
					return;
				const username = (this.user.title == null || this.user.title === "" ? "" : this.user.title + " ") + this.user.firstname + " " + this.user.lastname;
				authservice.createUser(this.user.email, username, this.password)
					.then(() => {
						this.isRegister = false;
						setImmediate((() => this.$refs.textfieldEMail.focus()).bind(this));
						this.dialogs.registrationSuccessfulDialog.dialog.open("E-Mail bestätigen", "Wir haben eine Verifikations-E-Mail an Sie versendet, die einen Verifikationslink enthält. Bitte überprüfen Sie Ihr Postfach und klicken Sie auf den Link, um Ihr Konto zu aktivieren.", [{text: "Schließen", color: "green"}])
					})
					.catch(err => {
						console.log(err);
						if(err.status === 400 || err.body != null) {
							if(err.body.error != null && typeof(err.body.error[0]) === "string") {
								this.errorMessage = "Das verwendete Passwort ist nicht gültig: " + err.body.error[0];
								return;
							}
							for(let key in Object.keys(err.body)) {
								if(err.body[key] != null && typeof(err.body[key][0]) === "string") {
									this.errorMessage = err.body[key][0];
									return;
								}
							}
						}
						this.errorMessage = "Es ist ein unerwarteter Fehler bei der Registrierung aufgetreten.";
					});
			},
			handleLoginResponse(loginResponse) {
				if(!session.importToken(loginResponse.tokens.access, loginResponse.tokens.refresh)
					|| !session.storeToken())
					throw {status: 400, message: "Failed to handle login response"};
				session.setExtraUserEMail(loginResponse.email);
				this.$router.push({name: "main"});
			}
		}
	};

</script>
