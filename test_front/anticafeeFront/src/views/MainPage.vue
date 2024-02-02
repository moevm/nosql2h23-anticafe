<template>
    <v-container fluid>
        <v-card height="81dvh" flat style="background-color: transparent;">
            <v-row>
                <v-col cols="12">
                    <v-carousel height="250">
                        <v-carousel-item
                        v-for="(item,i) in carouselItems"
                        :key="i"
                        :src="item.src"
                        cover
                        />
                    </v-carousel>
                </v-col>
                <v-col cols="6">
                    <v-card class="mx-auto">
                        <v-img 
                            class="align-top text-white"
                            height="200"
                            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                            cover
                        >
                            <v-card-title>Свободных столиков: {{ freeTablesCount }}</v-card-title>
                        </v-img>
                    </v-card>
                </v-col>
                <v-col cols="6">
                    <v-card class="mx-auto">
                        <v-img 
                            class="align-top text-white"
                            height="200"
                            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                            cover
                        >
                            <v-card-title>Игры</v-card-title>
                        </v-img>
                    </v-card>
                </v-col>
                <v-col cols="12">
                    <v-card class="mx-auto d-flex align-center justify-center"
                        image="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                        height="250"
                    >
                        <v-card-title class="justify-center text-white">Меню</v-card-title>
                    </v-card>
                </v-col>
            </v-row>
        </v-card>
    </v-container>
</template>

<script>

export default {
	name: 'MainPage',

	data() {
		return {
            page: 1,

            carouselItems: [
                {
                    src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
                },
                {
                    src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
                },
                {
                    src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
                },
                {
                    src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
                },
            ],
            
            freeTablesCount: 14, //should be taken from the DB
        }
	},

	methods: {

	},

  }

</script>