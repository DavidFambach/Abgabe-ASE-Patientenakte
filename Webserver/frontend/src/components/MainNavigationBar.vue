<template>
	<v-app-bar app color="primary" flat>
		
		<v-img class="shrink mr-2" width="40" alt="Logo"
			transition="scale-transition" contain
			src="@/assets/logo.svg" />
		
		<v-btn depressed href="./">Dateiansicht</v-btn>
		<v-btn depressed v-on:click.stop="openShareDialog()">Aktive Freigaben</v-btn>
		<v-btn depressed v-on:click.stop="openContactsDialog()">Kontakte verwalten</v-btn>
		
		<v-spacer />

		<v-menu bottom min-width="200px" rounded offset-y>
			<template v-slot:activator="{ on }">
				<v-btn icon x-large v-on="on">
					<v-avatar v-if="userinfo.nameAbbreviation != null" color="brown">
						<span class="white--text text-h5">{{ userinfo.nameAbbreviation }}</span>
					</v-avatar>
				</v-btn>
			</template>
			<v-card>
				<v-list-item-content class="justify-center">
					<div class="mx-auto text-center">
						
						<v-avatar v-if="userinfo.nameAbbreviation != null" color="brown">
							<span class="white--text text-h5">{{ userinfo.nameAbbreviation }}</span>
						</v-avatar>

						<h3>{{ userinfo.name }}</h3>
						<p v-if="userinfo.email != null" class="text-caption mt-1">
							{{ userinfo.email }}
						</p>
						<p v-if="userinfo.id != null" class="text-caption mt-1">
							Benutzernr.: {{ userinfo.id }}
						</p>

						<v-divider class="my-1" />
						
						<v-btn depressed text v-on:click="logOut">Ausloggen</v-btn>

						<v-divider class="my-1" />
						
						<v-btn depressed text
							v-on:click="() => dialogs.changePasswordDialog.dialog.open('Passwort ändern', '', [{text: 'Abbrechen'}, {text: 'Passwort ändern', color: 'green', onclick: changePassword}])">
							Passwort ändern
						</v-btn>
						
						<v-divider class="my-1" />

						<v-btn depressed text color="red"
							v-on:click="() => dialogs.confirmDeleteUserDialog.dialog.open('Benutzerkonto löschen', 'Sind Sie sicher, dass Sie Ihr Benutzerkonto einschließlich aller Daten in Ihrem Profil unwiderruflich löschen möchten? Wenn Sie Daten explizit für ein anderes Profil hochgeladen haben, werden diese Daten nicht gelöscht.', [{text: 'Abbrechen'}, {text: 'Alle Daten löschen', color: 'red', onclick: deleteUser}])">
							Benutzerkonto löschen
						</v-btn>
						
					</div>
				</v-list-item-content>
			</v-card>
		</v-menu>

        <action-dialog ref="changePasswordDialog"
			:prepare="() => {
				dialogs.changePasswordDialog.oldPassword = '';
				dialogs.changePasswordDialog.newPassword = '';
				dialogs.changePasswordDialog.newPasswordRepeated = '';
			}">
			<template v-slot:extra>
				<v-text-field label="Altes Passwort" placeholder="Passwort" color="secondary"
					v-model="dialogs.changePasswordDialog.oldPassword"/>
				<v-text-field key="textfieldPassword"
					name="Passwort" label="Passwort"
					placeholder="Passwort" color="light grey"
					required v-model="dialogs.changePasswordDialog.newPassword"
					:rules="[
						dialogs.changePasswordDialog.rules.notEmpty,
						dialogs.changePasswordDialog.rules.validPassword
					]" :type="dialogs.changePasswordDialog.showPassword ? 'text' : 'password'">
					<template v-slot:append>
						<v-btn icon tabindex="-1"
							v-on:click.stop="() => {dialogs.changePasswordDialog.showPassword = !dialogs.changePasswordDialog.showPassword}">
							<v-icon>{{dialogs.changePasswordDialog.showPassword ? "mdi-eye-off" : "mdi-eye"}}</v-icon>
						</v-btn>
					</template>
				</v-text-field>
				<v-text-field key="textfieldRepeatPassword"
					name="Passwort bestätigen" label="Passwort bestätigen"
					placeholder="Passwort bestätigen" type="password" color="light grey"
					required v-model="dialogs.changePasswordDialog.newPasswordRepeated"
					:rules="[
						dialogs.changePasswordDialog.rules.notEmpty,
						dialogs.changePasswordDialog.rules.validPassword,
						dialogs.changePasswordDialog.rules.matchesPassword
					]" />
			</template>
        </action-dialog>
		<action-dialog ref="confirmDeleteUserDialog" />

	</v-app-bar>
</template>

<script>

	import ActionDialog from "@/components/ActionDialog.vue";
	import * as authservice from "@/authservice";
	import * as fileservice from "@/fileservice";
	import * as session from "@/session";

	function getNameAbbreviation(name) {
		if(name == null)
			return null;
		const names = name.match(/\b(\w+)(?!\.)\b/g);
		if(names.length === 0)
			return null;
		if(names.length === 1)
			return names[0].substring(0, 1).toUpperCase();
		return names[0].substring(0, 1).toUpperCase() + names[names.length - 1].substring(0, 1).toUpperCase();
	}

	export default {
		name: "main-navigation-bar",
		components: {
			ActionDialog
		},
		props: {
            displayMessage: Function,
			openContactsDialog: Function,
			openShareDialog: Function
		},
		mounted() {

			this.dialogs.changePasswordDialog.dialog = this.$refs.changePasswordDialog;
			this.dialogs.confirmDeleteUserDialog.dialog = this.$refs.confirmDeleteUserDialog;

			this.userinfo.id = session.getUserID();
			this.userinfo.email = session.getExtraUserEMail();
			fileservice.getContactName(this.userinfo.id)
				.then((contactResponse => {
					this.userinfo.name = contactResponse.contact.displayName;
					this.userinfo.nameAbbreviation = getNameAbbreviation(this.userinfo.name);
				}).bind(this))
				.catch(console.log);
			
		},
		data() {
			return {
				dialogs: {
					changePasswordDialog: {
						dialog: null,
						oldPassword: "",
						newPassword: "",
						newPasswordRepeated: "",
						showPassword: false,
						rules: {
							notEmpty: value => value == null || value === "" ? "Dieses Feld ist erforderlich" : true,
							validPassword: value => typeof(value) !== "string" || value.match(/^.{6,}$/) == null ? "Das Passwort muss mindestens 6 Zeichen lang sein" : true,
							matchesPassword: value => value !== this.dialogs.changePasswordDialog.newPassword ? "Die Passwörter stimmen nicht überein" : true
						}
					},
					confirmDeleteUserDialog: {
						dialog: null
					}
				},
				userinfo: {
					id: null,
					name: null,
					nameAbbreviation: null,
					email: null
				}
			};
		},
		methods: {
			changePassword() {
				this.displayMessage({userMessage: "Diese Operation wird noch nicht unterstützt."});
			},
			deleteUser() {
				authservice.deleteUser(session.getRefreshToken())
					.then(() => {
						session.logOut().catch(() => undefined)
							.then(() => this.$router.push({name: "login"}));
					}).catch(err => this.displayMessage({message: "Failed to delete user"}, err));
			},
			logOut() {
				session.logOut()
					.then(() => this.$router.push({name: "login"}))
					.catch(err => this.displayMessage({message: "Failed to log out"}, err));
			}
		}
	}

</script>
