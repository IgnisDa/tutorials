<template>
  <div class="container mx-auto my-10">
    <form class="flex flex-col space-y-10" @submit.prevent="handleSubmit">
      <input
        v-model="formData.email"
        class="border-2 border-black"
        placeholder="email"
        required
        type="email"
      />
      <input
        v-model="formData.password"
        class="border-2 border-black"
        placeholder="password"
        required
        type="password"
      />
      <button type="submit" class="bg-red-500 p-3 text-xl">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        email: '',
        password: '',
      },
    }
  },
  methods: {
    async handleSubmit() {
      const formData = new FormData()
      formData.append('email', this.formData.email)
      formData.append('password', this.formData.password)
      const data = await this.$http.$post('/accounts/create/', formData)
      console.log(data)
    },
  },
}
</script>
