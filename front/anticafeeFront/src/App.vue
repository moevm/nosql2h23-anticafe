<template>
	<v-app style="background-color: #F5F5F9">
		
		<v-navigation-drawer 
			permanent
			theme="dark" 
			class="main-menu"
			app
		>
			<v-list-item>
				<div style="text-align: center;">
					<v-icon class="mx-auto mb-n3" size="92">mdi-coffee-outline</v-icon>
					<h1 style="font-size: 42px;">Anticafe</h1>
				</div>
			</v-list-item>
			<div v-show="!isLoggedIn">
				<v-list-item link title="Бронь стола" prepend-icon="mdi-phone" @click="openLogin()"></v-list-item>
				<v-list-item link title="Регистрация" prepend-icon="mdi-exit-to-app" @click="openSignup()"></v-list-item>
			</div>
		</v-navigation-drawer>
		<v-app-bar app flat border height="100" clipped-left>
			<v-row class="ma-10">
				<v-col cols="11">
					<v-btn block rounded variant="outlined">Заказать столик</v-btn>
				</v-col>
				<v-col v-if="!isLoggedIn" align="center">
					<v-btn rounded>Войти</v-btn>
				</v-col>
				<v-col v-else align="center" class="mr-n12">
					<a style="font-size: 18px;">{{ userName }}</a>
					<v-icon size="36" class="mx-1">mdi-account-circle</v-icon>
				</v-col>
			</v-row>
		</v-app-bar>
		
		<v-main class="d-flex align-center justify-center ma-2">
			<router-view/>
			<!--main-page/-->
		</v-main>
	</v-app>

</template>

<script>
	import MainPage from '@/components/MainPage.vue';

	export default {
	name: 'App',

	data() {
		return {
		page: 1,
		
		isLoggedIn: false,
		loginToggle: false,
		signupToggle: false,

		userName: 'Test Username', //get current username 
		}
	},

	methods: {
		openLogin() {
			this.loginToggle = true;
		},

		openSignup() {
			this.signupToggle = true;
		}

	},

  }

</script>

<style lang="scss">

.main-menu {
	background-color: #363740 !important;
}

</style>
