<template>
	<v-app style="background-color: #F5F5F9">
		
		<v-navigation-drawer 
			permanent
			theme="dark" 
			class="main-menu"
			app
		>
			<x-drawer :current-user="userType"/> <!--Dynamic nav tab depending on the user type-->
		</v-navigation-drawer>

		<v-app-bar app flat border height="100" clipped-left>
			<v-row class="ma-10">
				<v-col cols="11">
					<v-btn block rounded variant="outlined" @click="bookTable()">Заказать столик</v-btn>
				</v-col>
				<v-col v-if="!isLoggedIn" align="center">
					<v-btn rounded @click="openLogin()">Войти</v-btn>
				</v-col>
				<v-col v-else align="center" class="mr-n12">
					<a style="font-size: 16px;">{{ userName }}</a>
					<v-icon size="36" class="mx-1">mdi-account-circle</v-icon>
				</v-col>
			</v-row>
		</v-app-bar>

		<v-dialog v-model="dialog" max-width="40dvw">
			<v-card>
				<v-row class="ma-5" v-if="loginToggle" justify="center" align="center">
					<v-col cols="12">
						<v-text-field
							label="Login"
							prepend-icon="mdi-account"
							variant="outlined"
						></v-text-field>
					</v-col>
					<v-col cols="12">
						<v-text-field
							label="Password"
							prepend-icon="mdi-key"
							variant="outlined"
						></v-text-field>
					</v-col>
					<v-col cols="auto">
						<v-btn rounded width="200" @click="userLoginHandle()">Войти</v-btn>
					</v-col>
					<v-col cols="auto">
						<v-btn rounded width="200" @click="openSignup()">Регистрация</v-btn>
					</v-col>
				</v-row>
				<v-row class="ma-5" v-if="signupToggle" justify="center" align="center">
					<v-col cols="12">
						<v-text-field
							label="e-mail"
							prepend-icon="mdi-mail-ru"
							variant="outlined"
							v-model="emailInput"
						></v-text-field>
					</v-col>
					<v-col cols="12">
						<v-text-field
							label="Login"
							prepend-icon="mdi-account"
							variant="outlined"
							v-model="usernameInput"
						></v-text-field>
					</v-col>
					<v-col cols="12">
						<v-text-field
							label="Password"
							prepend-icon="mdi-key"
							variant="outlined"
							v-model="userPasswordInput"
						></v-text-field>
					</v-col>
					<v-col cols="12">
						<v-text-field
							label="Confirm password"
							variant="outlined"
						></v-text-field>
					</v-col>
					<v-col cols="6">
						<v-btn class="mx-1" rounded @click="closeDialog()" >Отмена</v-btn>
					</v-col>
					<v-col cols="6">
						<v-btn class="mx-1" rounded @click="userLoginHandle()">Ок</v-btn>
					</v-col>
				</v-row>
			</v-card>
		</v-dialog>
		
		<v-main class="d-flex align-center justify-center ma-2">
			<router-view/>
		</v-main>
	</v-app>

</template>

<script>
	import XDrawer from '@/components/shared/XDrawer.vue';

	export default {
	name: 'App',
	components: {
		XDrawer,
	},

	computed: {
		dialog() {
			if (this.loginToggle || this.signupToggle) return true
			return false
		}
	},

	watch: {
		isLoggedIn: {
			handler (newV, oldV) {
				if (newV) this.bookTable();
			}
		},
	},

	data() {
		return {
		page: 1,

		isLoggedIn: false,
		loginToggle: false,
		signupToggle: false,

		usernameInput: '',
		userPasswordInput: '',
		emailInput: '',

		userName: 'Test Username', //get current username 
		userType: ''//'customer', //get current user type: customer, admin, employee
		}
	},

	methods: {
		openLogin() {
			this.signupToggle = false;
			this.loginToggle = true;
		},

		openSignup() {
			this.loginToggle = false;
			this.signupToggle = true;
		},

		closeDialog() {
			this.signupToggle = false;
			this.loginToggle = false;
		},
		
		userLoginHandle() { //WIP => POST data to get OK on the AUTH
			this.userType = 'customer'; //TEST DATA
			this.isLoggedIn = true; //TEST DATA

			this.closeDialog();
		},

		bookTable() {
			if (this.isLoggedIn) {
				this.$router.push('/book')
				return;
			} //WIP => HANDLE ROUTER
			else {
				this.openLogin();
			}
		}

	},

  }

</script>

<style lang="scss">

.main-menu {
	background-color: #363740 !important;
}

</style>
