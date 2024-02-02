<template>
  <v-container fluid>
    <v-card height="81dvh">
      <v-row class="ma-5">
        <v-col cols="12" >
          <v-card flat border style="background-color: transparent !important;" height="74vh">
            <v-data-table
                fixed-header
                height="60vh"
                :headers="headers"
                :items="items"
            >
              <template v-slot:top>
                <v-toolbar flat color="#F5F5F9">
                  <v-btn></v-btn>
                  <v-btn></v-btn> <!--WIP: Filters for the table (date, time, capacity, console)-->
                </v-toolbar>
              </template>
              <template v-slot:loading>
                <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
              </template>
              <template v-slot:item.actions="{ item }">
                <v-btn density="compact" size="small"  flat border :disabled="!item.action" @click="workTable(item)">Выбрать</v-btn>
              </template>
              <template v-slot:item.name="{ value }">
                <v-chip label color="indigo">
                  {{ value }}
                </v-chip>
              </template>
              <template v-slot:item.action="{ value }">
                <v-chip variant="text" :color="getColor(value)">
                  {{ getStatusValue(value) }}
                </v-chip>
              </template>
              <template v-slot:item.status="{ value }">
                <v-chip variant="text" :color="getColor(value)">
                  {{ getStatusValue(value) }}
                </v-chip>
              </template>
              <template v-slot:item.delete="{ index }">
                <v-btn density="compact" size="small" @click="deleteTable(index)">Удалить</v-btn>
              </template>
            </v-data-table>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>

export default {
  name: 'WorkTable',

  data: () => ({
    searchActivated: false,
    searchFilter: false,

    searchListPreset: [
      {'value':'name', 'text': 'Имя'},
      {'value':'date', 'text': 'Дата'},
      {'value':'status', 'text': 'Статус'},
    ],

    searchFieldList: [0,1,2,3],

    headers: [
      {
        title: 'Выбрать',
        align: 'center',
        key: 'actions',
        sortable: false
      },
      {
        title: 'Имя работника',
        sortable: true,
        key: 'info',
      },
      {
        title: 'Статус',
        key: 'status',
        sortable: false
      },
      {
        title: '',
        key: 'delete',
        align: 'center',
        sortable: false
      },
    ],

    items: [
      {
        action: true,
        info: 'John Doe',
        status: true
      },                {
        action: true,
        info: '1John Doe',
        status: true
      },                {
        action: true,
        info: '2John Doe',
        status: true
      },                {
        action: true,
        info: '3John Doe',
        status: true
      },                {
        action: true,
        info: '4John Doe',
        status: true
      },                {
        action: true,
        info: '5John Doe',
        status: true
      },

    ],

    itemsOptions: {
      page: 1,
      itemsPerPage: 30,
      sortBy: [],
      sortDesc: [],
      groupBy: [],
      groupDesc: [],
      multiSort: true,
      mustSort: false,
      searchData: '',
      searchFields: [],
      ranks: [],
    },

    isClean: true,
    itemLookupData: '',
    localStorageExists: false,

  }),

  methods: {
    workTable(item) { //WIP => POST table data to BOOK it
      console.log('work ', item.number);
      item.status = false;
    },
    deleteTable(index) {
      this.items.splice(index, 1);
    },

    getColor(value) {
      if (value) return 'black'
      return 'grey'
    },

    getStatusValue(value) {
      if (value) return 'Работает'
      return 'Отсутствует'
    },

  }

}

</script>

<style>
::v-deep .v-data-table-header {
  background-color: rgb(177, 85, 85) !important;
}

</style>