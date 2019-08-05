<template>
  <div class="content">
    <content-title icon="signup-form" title="Prijava organizacije" />

    <h1>Add organization</h1>

    <form action method="POST" @submit.prevent="onSubmit">
      <label for="name">Name:</label>
      <input id="name" name="name" />
      <br />
      <label for="description">Description:</label>
      <textarea id="description" name="description" rows="4" />
      <br />
      <label for="image">Image:</label>
      <input id="image" name="cover_photo" type="file" />
      <br />
      <br />
      <input type="submit" value="Submit" />
    </form>
  </div>
</template>

<script>
import ContentTitle from '~/components/ContentTitle.vue';

export default {
  components: {
    ContentTitle,
  },
  methods: {
    async onSubmit(event) {
      try {
        const form = event.target;
        const formData = new FormData(form);
        const org = await this.$axios.$post('http://127.0.0.1:8000/api/organizations/', formData);
        this.$router.push({
          name: 'org-id',
          params: { id: org.id },
          query: { edit_key: org.edit_key },
        });
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
        alert(error.message);
      }
    },
  },
  head() {
    return {
      title: 'Prijava organizacije',
    };
  },
};
</script>

<style lang="scss" scoped>
.container {
  margin: 20px auto 0;
  max-width: 900px;

  label {
    display: block;
    margin: 1rem 0 0.25rem;
  }

  input,
  textarea {
    width: 100%;
    max-width: 500px;
    padding: 0.25rem 0.5rem;
    border: 1px solid #ccc;
  }
}
</style>
