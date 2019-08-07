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
            <text-input name="name" label="Uradno ime organizacije (iz AJPES)" />
            <text-input
              name="additional_names"
              label="Druga imena, pod katerimi je organizacija poznana (kratice, okrajšave)"
            />
          </form-category>
          <form-category title="Kontakt">
            <text-input name="contact__name" label="Ime in priimek" />
            <text-input name="contact__email" label="E-naslov" />
            <text-input name="contact__phone" label="Telefon" />
          </form-category>
          <form-category title="Spletna prisotnost">
            <text-input name="web_page" label="URL spletne strani" />
            <text-input name="social_media" label="URL profila na družbenem mediju" />
            <strong>
              TODO: + button for more social links
              <br />
              <br />
            </strong>
          </form-category>
          <form-category title="Slika">
            <strong>
              TODO: upload button za sliko
              <br />
              <br />
            </strong>
          </form-category>
          <form-category title="Poslanstvo" note="največ 500 znakov">
            <text-input name="mission" :multiline="9" />
          </form-category>
          <form-category title="Kratek opis" note="največ 1500 znakov">
            <text-input name="description" :multiline="27" />
          </form-category>
          <form-category title="Področja delovanja" note="lahko izberete več možnosti">
            <radio-option
              name="area"
              value="equality"
              label="Človekove pravice, demokracija in enakost"
            />
            <radio-option name="area" value="edu" label="Izobraževanje, raziskave in razvoj" />
            <radio-option name="area" value="culture" label="Kultura" />
            <radio-option name="area" value="youth" label="Mladina, otroci" />
            <radio-option name="area" value="development" label="Razvojno sodelovanje" />
            <radio-option name="area" value="social" label="Sociala" />
            <radio-option name="area" value="sport" label="Šport" />
            <radio-option name="area" value="environment" label="Okolje, narava in prostor" />
            <radio-option name="area" value="health" label="Zdravje" />
            <radio-option name="area" value="other" label="Drugo (navedite kaj):" />
          </form-category>

          <form-category>
            <span>avg_revenue</span>
            <div>povprečni letni proračun v zadnjih treh letih</div>
            <span>employed</span>
            <div>število zaposlenih v zadnjem zaključenem letu</div>
          </form-category>

          <form-category title="Statusi">
            <radio-option
              name="is_charity"
              label="Organizacija ima status humanitarne organizacije"
            />
            <radio-option
              name="has_public_interest"
              label="Organizacija ima status delovanja v javnem interesu"
            />
            <radio-option
              name="is_voluntary"
              label="Organizacija je vpisana v evidenco prostotovoljskih organizacij"
            />
            <radio-option
              name="zero5"
              label="Organizacija je na seznamu upravičencev do 0,5 % dohodnine"
            />
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
