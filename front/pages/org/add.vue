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
            <add-button text="Dodaj družbeni profil" />
          </form-category>

          <form-category title="Slika">
            <file-input name="cover_photo" />
          </form-category>

          <form-category title="Poslanstvo" note="največ 500 znakov">
            <text-input name="mission" :multiline="9" />
          </form-category>

          <form-category title="Kratek opis" note="največ 1500 znakov">
            <text-input name="description" :multiline="27" />
          </form-category>

          <form-category title="Področja delovanja" note="lahko izberete več možnosti">
            <selection-option
              type="checkbox"
              name="area"
              value="equality"
              label="Človekove pravice, demokracija in enakost"
            />
            <selection-option
              type="checkbox"
              name="area"
              value="education"
              label="Izobraževanje, raziskave in razvoj"
            />
            <selection-option type="checkbox" name="area" value="culture" label="Kultura" />
            <selection-option type="checkbox" name="area" value="youth" label="Mladina, otroci" />
            <selection-option
              type="checkbox"
              name="area"
              value="development"
              label="Razvojno sodelovanje"
            />
            <selection-option type="checkbox" name="area" value="social" label="Sociala" />
            <selection-option type="checkbox" name="area" value="sport" label="Šport" />
            <selection-option
              type="checkbox"
              name="area"
              value="environment"
              label="Okolje, narava in prostor"
            />
            <selection-option type="checkbox" name="area" value="health" label="Zdravje" />
            <selection-option
              type="checkbox"
              name="area"
              value="other"
              label="Drugo (navedite kaj):"
            />
          </form-category>

          <form-category title="Proračun">
            <text-input name="avg_revenue" label="Povprečni letni proračun v zadnjih treh letih" />
            <text-input name="employed" label="Število zaposlenih v zadnjem zaključenem letu" />
          </form-category>

          <form-category title="Statusi">
            <selection-option
              type="checkbox"
              name="is_charity"
              label="Organizacija ima status humanitarne organizacije"
            />
            <selection-option
              type="checkbox"
              name="has_public_interest"
              label="Organizacija ima status delovanja v javnem interesu"
            />
            <selection-option
              type="checkbox"
              name="is_voluntary"
              label="Organizacija je vpisana v evidenco prostotovoljskih organizacij"
            />
            <selection-option
              type="checkbox"
              name="zero5"
              label="Organizacija je na seznamu upravičencev do 0,5 % dohodnine"
            />
          </form-category>
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
import SelectionOption from '~/components/Form/SelectionOption.vue';
import AddButton from '~/components/Form/AddButton.vue';
import FileInput from '~/components/Form/FileInput.vue';

export default {
  components: {
    ContentTitle,
    FormStages,
    FormCategory,
    TextInput,
    SelectionOption,
    AddButton,
    FileInput,
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
  }
}
</style>
