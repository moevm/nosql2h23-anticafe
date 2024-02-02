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
							<template v-slot:item.number="{ value }">
								<v-chip label color="indigo">
									{{ value }}
								</v-chip>
							</template>
							<template v-slot:item.status="{ value }">
								<v-chip variant="text" :color="getColor(value)">
									{{ getStatusValue(value) }}
								</v-chip>
							</template>
							<template v-slot:item.console="{ value }">
								<v-chip variant="text">
									{{ getConsoleValue(value) }}
								</v-chip>
							</template>
              <template v-slot:item.delete="{ index }">
                <v-btn density="compact" size="small" @click="deleteTable(index)">Удалить</v-btn>
              </template>
							<template v-slot:item.actions="{ item }">
                                <v-btn density="compact" size="small" flat border :disabled="!item.status" @click="gameTable(item)">Записаться</v-btn>
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
    name: 'GameTable',

	data: () => ({
		searchActivated: false,
        searchFilter: false,

		searchListPreset: [
			{'value':'capacity', 'text': 'Кол-во человек'},
			{'value':'date', 'text': 'Дата'},
			{'value':'time', 'text': 'Время'},
			{'value':'console', 'text': 'Наличие приставки'},
		],

		searchFieldList: [0,1,2,3],

		headers: [
			{
				title: 'Название',
				align: 'center',
				key: 'name',
				sortable: true
			},
			{
				title: 'Кол-во человек',
				align: 'center',
				sortable: true,
				key: 'capacity',
			},
			{
				title: 'Статус',
				align: 'center',
				key: 'status',
				sortable: false
			},
			{
				title: '',
				key: 'actions',
        align: 'center',
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
        name: "0Leti-Games",
				capacity: 2,
				status: true
			},                {
        name: "1Leti-Games",
				capacity: 10,
				status: true
			},                {
        name: "2Leti-Games",
				capacity: 10,
				status: false
			},                {
        name: "3Leti-Games",
				capacity: 2,
				status: false
			},                {
        name: "4Leti-Games",
				capacity: 3,
				status: true
			},                {
        name: "5Leti-Games",
				capacity: 4,
				status: false,
			},{
        name: "6Leti-Games",
				capacity: 4,
				status: false
			},{
        name: "7Leti-Games",
				capacity: 7,
				status: true
			},{
        name: "8Leti-Games",
				capacity: 5,
				status: true
			},{
        name: "9Leti-Games",
				capacity: 5,
				status: false
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
		gameTable(item) { //WIP => POST table data to BOOK it
			console.log('game ', item.number);
			item.status = false;
		},

		getColor(value) {
			if (value) return 'green'
			return 'red'
		},

		getStatusValue(value) {
			if (value) return 'Свободен'
			return 'Занят'
		},

		getConsoleValue(value) {
			if (value) return 'Есть'
			return 'Нет'
		},

    deleteTable(index) {
      this.items.splice(index, 1);
    }
	}

}

</script>

<style>
::v-deep .v-data-table-header {
	background-color: rgb(177, 85, 85) !important;
}

</style>