<template>
  <div class="content">
    <content-title icon="signup-form" title="Prijava organizacije" />
    <div class="row justify-content-center">
      <div class="col-12 col-md-7 col-xxl-5">
        <form-stages />
      </div>
    </div>
    <div class="row justify-content-center form-row">
      <div class="col-12 col-md-7 col-xxl-5">
        <form @submit.prevent>
          <form-category title="Ime">
            <text-input name="orgName" label="Uradno ime organizacije" />
            <text-input name="orgNameOther" label="Druga imena" />
          </form-category>
          <form-category title="Kontakt">
            <text-input
              name="orgPhone"
              label="Telefon"
              value="+00 00 000 00 00"
              has-error="nepravilna telefonska številka"
            />
          </form-category>
          <form-category title="Poslanstvo" note="največ 500 znakov">
            <text-input name="orgDesc" multiline />
          </form-category>
          <form-category title="Področja delovanja" note="lahko izberete več možnosti">
            <radio-option name="cr" value="this" label="this custom radio" />
            <radio-option name="cr" value="that" label="that custom radio" />
            <radio-option name="cr" value="other" label="other custom radio" />
            <radio-option name="cr" value="custom" label="Drugo:" />
          </form-category>

          <fieldset>
            <legend>Člani</legend>

            <div>
              <button class="btn btn-outline-primary btn-form icon icon-add">Dodaj člana</button>
            </div>
            <br />

            <div class="custom-file">
              <input id="customFile" type="file" class="custom-file-input" />
              <label class="custom-file-label icon icon-upload" for="customFile">
                <span>Naloži datoteko</span>
              </label>
            </div>
          </fieldset>
        </form>
      </div>
    </div>

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
import FormStages from '~/components/FormStages.vue';
import FormCategory from '~/components/Form/FormCategory.vue';
import TextInput from '~/components/Form/TextInput.vue';
import RadioOption from '~/components/Form/RadioOption.vue';

export default {
  components: {
    ContentTitle,
    FormStages,
    FormCategory,
    TextInput,
    RadioOption,
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
.content {
  .form-row {
    margin-top: 6rem;

    .custom-control:last-of-type {
      margin-bottom: 3rem;
    }

    .btn-form {
      border-width: 2px;
      border-radius: 0.41em;
      font-weight: 700;
      font-size: 1.5rem;
      color: $body-color;
      letter-spacing: 0.2em;
      width: auto;
      height: 5rem;
      padding: 1rem 1.5rem 1rem 5rem;
      background-position: left center;
      background-size: 5rem 45%;
    }

    .custom-file {
      width: auto;

      &,
      .custom-file-input,
      .custom-file-label {
        height: 5rem;
      }

      .custom-file-input {
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        cursor: pointer;
      }

      .custom-file-label {
        position: relative;
        display: flex;
        align-items: center;
        width: 100%;
        margin: 0;
        border-width: 2px;
        border-radius: 0.41em;
        border-color: $blue;
        font-weight: 700;
        font-size: 1.5rem;
        color: $body-color;
        letter-spacing: 0.2em;
        padding: 1rem 1.5rem 1rem 5rem;
        background-position: left center;
        background-size: 5rem 45%;

        &::after {
          display: none;
        }
      }

      .custom-file-input:hover ~ .custom-file-label {
        background-color: $blue;
      }
    }
  }
}
</style>
