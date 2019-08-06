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
            <br />
          </form-category>

          <fieldset>
            <div class="custom-control custom-radio">
              <input id="cr1" type="radio" name="cr" class="custom-control-input" />
              <label class="custom-control-label" for="cr1">this custom radio</label>
            </div>
            <div class="custom-control custom-radio">
              <input id="cr2" type="radio" name="cr" class="custom-control-input" />
              <label class="custom-control-label" for="cr2">other custom radio</label>
            </div>
            <div class="custom-control custom-radio">
              <input id="cr3" type="radio" name="cr" class="custom-control-input" />
              <label class="custom-control-label d-flex align-items-center" for="cr3">
                Drugo:
                <input class="form-control" />
              </label>
            </div>
          </fieldset>
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
import TextInput from '~/components/Form/TextInput.vue';
import FormCategory from '~/components/Form/FormCategory.vue';

export default {
  components: {
    ContentTitle,
    FormStages,
    TextInput,
    FormCategory,
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

    .custom-radio,
    .custom-checkbox {
      padding-left: 2.5rem;

      .custom-control-label {
        font-size: 1.85rem;
        font-weight: 300;
        height: 4rem;
        display: flex;
        align-items: center;

        &::before,
        &::after {
          width: 1.75rem;
          height: 1.75rem;
          top: 1.125rem;
          left: -2.5rem;
          cursor: pointer;
        }

        &::before {
          border-width: 2px;
        }

        &.d-flex {
          .form-control {
            margin-left: 1.5rem;
            border: 0;
            background: rgba(#f6f2f0, 0.4);
            font-size: 1.5rem;
            font-weight: 300;
            padding: 0.5rem 1.75rem;
            border-bottom: 2px solid rgba($blue, 0.3);
            height: 4rem;

            &,
            &:focus {
              outline: 0;
              box-shadow: none;
            }

            &:focus {
              border-bottom-color: $blue;
            }
          }
        }
      }

      .custom-control-input ~ .custom-control-label::before {
        border-color: $blue;
      }

      .custom-control-input:checked ~ .custom-control-label::before {
        background-color: #fff;
      }

      .custom-control-input:checked ~ .custom-control-label::after {
        background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-10 -10 20 20'%3e%3ccircle r='5.5' fill='%23#{str-slice(#{$blue}, 2)}'/%3e%3c/svg%3e");
        background-size: contain;
        background-position: center;
      }
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
