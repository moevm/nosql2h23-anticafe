<template>
    <div style="float: right;">
        <h1>MainPage</h1>
<v-btn>заказать столик</v-btn>
<v-btn>войти</v-btn>
<v-card>свободных столов</v-card>
<!-- Всплывающая регистрация -->
        <v-dialog width="500">
            <template v-slot:activator="{ props }">
                <v-btn v-bind="props" text="Open Dialog"> </v-btn>
            </template>

            <template v-slot:default="{ isActive }">
                <v-card>
                <v-card-actions>
                    <v-spacer></v-spacer>
                
                    <v-sheet width="300" class="mx-auto">
                        <v-form fast-fail @submit.prevent>
                        <v-text-field
                            clearable
                            v-model="firstName"
                            label="Name"
                            :rules="nameRules"
                            prepend-icon="`mdiSvg:${mdiAccount}`"
                        ></v-text-field>

                        <v-text-field
                            clearable
                            v-model="lastName"
                            label="email"
                            :rules="emailRules"
                            prepend-icon="`mdiSvg:${mdiAccount}`"
                        ></v-text-field>

                        <v-btn type="submit" block class="mt-2">Войти</v-btn>
                        <v-btn text="Регистрация"></v-btn>
                        </v-form>
                    </v-sheet>

                    <!-- <v-btn
                    text="Войти"
                    @click="isActive.value = false"
                    ></v-btn>
                    <v-btn
                    text="Регистрация"
                    @click="isActive.value = false"
                    ></v-btn> -->
                </v-card-actions>
                </v-card>
            </template>
        </v-dialog>
    </div>
    <v-carousel style="width: 300px; float: right;"></v-carousel>
    <Leftnav/>
</template>

<script>

</script>