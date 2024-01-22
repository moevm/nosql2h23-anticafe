import { createApp } from 'vue';
import App from './App.vue';
import store from './store/store';
import vuetify from './plugins/vuetify'
import router from "@/router";
import Leftnav from './components/Leftnav'


const app = createApp(App);
app.component('leftnav', Leftnav)
app.use(store);
app.use(vuetify);
app.use(router);
app.mount('#app');