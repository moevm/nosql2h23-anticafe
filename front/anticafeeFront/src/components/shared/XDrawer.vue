<template>
    <div>
        <v-list class="pa-0" dense>
            <v-list-item>
                <div style="text-align: center;">
                    <v-icon class="mx-auto mb-n3" size="92">mdi-coffee-outline</v-icon>
                    <h1 style="font-size: 42px;">Anticafe</h1>
                </div>
            </v-list-item>
            <v-list-item
                v-for="(item, i) in items"
                :key="i"
                :title="item.title"
                :prepend-icon="parseIcon(item.icon)"
            >
            </v-list-item>
        </v-list>
    </div>
</template>

<script>

export default {
    name:'XDrawer',
    props: {
        currentUser: {
            type: String,
            default: ""
        }
    },

  data: () => ({
    mini: false,

    itemsBeforeLog: [
        {
            title: 'Бронь стола',
            icon: 'phone'
        },
        {
            title: 'Регистрация',
            icon: 'exit-to-app'
        }
    ],

    itemsCustomer: [
        {
            title: 'Номер стола: 0000', //change depending on the current table state
            icon: 'account-check' 
        },
        {
            title: 'Выход', 
            icon: 'exit-to-app' 
        },
    ],

    itemsEmployee: [
        {
            title: 'Главная страница', 
            icon: 'account-check' 
        },
        {
            title: 'Список столов', //change depending on the current table state
            icon: 'exit-to-app' 
        },
        {
            title: 'Выход', 
            icon: 'exit-to-app' 
        },
    ],

    itemsAdmin: [
        {
            title: 'Главная страница', 
            icon: 'account-check' 
        },
        {
            title: 'Посадить за стол', //change depending on the current table state
            icon: 'exit-to-app' 
        },
        {
            title: 'Выход', 
            icon: 'exit-to-app' 
        },
    ]

  }),

  computed: {
    //mapState to track userData ETC...
    items() {
        if (this.currentUser === 'admin') return this.itemsAdmin;
        if (this.currentUser === 'customer') return this.itemsCustomer
        if (this.currentUser === 'employee') return this.itemsEmployee
        return this.itemsBeforeLog
    }
  },

  created() {
    //
  },

  methods: {
    parseIcon(name) {
      if (name == 'phone') {
        return 'mdi-phone'
      }
      if (name == 'exit-to-app') {
        return 'mdi-exit-to-app'
      }
      if (name == 'account-check') {
        return 'mdi-account-check'
      }
      if (name == 'reorder-horizontal') {
        return 'mdi-reorder-horizontal'
      }
      if (name == 'dots-vertical') {
        return 'mdi-dots-vertical'
      }
      if (name == 'dots-horizontal') {
        return 'mdi-dots-horizontal'
      }

      const pre = 'mdi-'
      return pre + name;
    },

    goTo(item) { //router use
      if (item.route) {
        this.$router.push(item.route)
        return;
      }
      if (item.url) {
        window.location = item.url;
        return;
      }

    }
  }

}

</script>