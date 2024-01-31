<template>
    <v-container fluid>
        <v-card height="81dvh">
            <v-row class="ma-5">
                <v-col cols="4">
                    <v-card flat border style="background-color: transparent !important;" class="d-flex align-center justify-center" height="74vh">
                        <v-card-title class="justify-center text-grey">Изображение: схема кафе</v-card-title>
                    </v-card>
                </v-col>
                <v-col cols="8" >
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
							<template v-slot:item.actions="{ item }">
                                <v-btn density="compact" size="small" flat border :disabled="!item.status" @click="bookTable(item)">Записаться</v-btn>
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
    name: 'BookTable',

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
				title: 'Номер стола',
				align: 'center',
				key: 'number',
				sortable: false
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
				title: 'Приставка',
				align: 'center',
				key: 'console',
				sortable: false
			},
			{ 
				title: '', 
				key: 'actions', 
				sortable: false
			},
		],

		items: [
			{
				number: 0,
				capacity: 3,
				status: true,
				console: false
			},                {
				number: 1,
				capacity: 5,
				status: true,
				console: true
			},                {
				number: 2,
				capacity: 10,
				status: false,
				console: true
			},                {
				number: 3,
				capacity: 4,
				status: false,
				console: false
			},                {
				number: 4,
				capacity: 5,
				status: true,
				console: false
			},                {
				number: 5,
				capacity: 4,
				status: false,
				console: false
			},{
				number: 6,
				capacity: 4,
				status: false,
				console: false
			},{
				number: 7,
				capacity: 4,
				status: true,
				console: false
			},{
				number: 8,
				capacity: 7,
				status: true,
				console: false
			},{
				number: 9,
				capacity: 3,
				status: false,
				console: false
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
		bookTable(item) { //WIP => POST table data to BOOK it
			console.log('book ', item.number);
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
		}
	}

}

</script>

<style>
::v-deep .v-data-table-header {
	background-color: rgb(177, 85, 85) !important;
}

</style>