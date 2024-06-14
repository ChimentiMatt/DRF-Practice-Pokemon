<template>
    <div class="bg-primary-blue h-screen">

        <form class="flex flex-col items-center w-full text-white" v-on:submit.prevent="submitForm">
            <div class="flex flex-col items-center drop-shadow-lg">
                <h1 class="text-[68px] lilitaFont text-primary-yellow mt-[2rem] sm:mt-[5rem] sm:text-[120px]">Bee Hive</h1>
                <h3 class="text-white">Create your acccount</h3>
            </div>

            <input v-model="form.name" label="Name" field="text" />

            <input v-model="form.email" label="Email" field="email" />

            <input v-model="form.password1" label="Password" field="password" />

            <input v-model="form.password2" label="Confirm Password" field="password" />


            <button>sign up</button>
        </form>

    </div>
</template>

<script>

import axios from 'axios';

export default {
    setup() {

        return {
            
        }
    },

    components: {

    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') this.errors.push('Your e-mail is missing')

            if (this.form.name === '') this.errors.push('Your name is missing')

            if (this.form.password1 === '') this.errors.push('Your password is missing')

            if (this.form.password1 !== this.form.password2) this.errors.push('The password does not match')

            if (this.errors.length === 0) {
                axios
                    .post('/accounts/signup/', this.form)
                    .then(response => {
                        if (response.data.status === 'success') {
                            console.log('success')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''

                        } else {
                            console.log('error')
                        }

                    })
                    .catch(error => {
                        console.log('error', error)

                    })
            } else {
            }
        },

    }
}
</script>