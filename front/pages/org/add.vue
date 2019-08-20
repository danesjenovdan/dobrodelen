<template>
  <div class="content">
    <content-title icon="signup-form" title="Prijava organizacije" />
    <div class="row justify-content-center">
      <div class="col-12 col-md-7 col-xxl-5">
        <form-stages
          ref="formStages"
          :stages="stages"
          :active="activeStage"
          @change="onChangeStage"
        />
      </div>
    </div>
    <div class="row justify-content-center form-row">
      <div class="col-12 col-md-7 col-xxl-5">
        <form ref="form" @submit.prevent>
          <template v-if="activeStage === 0">
            <form-category title="Ime">
              <text-input
                v-model="data[0].name"
                name="name"
                label="Uradno ime organizacije (iz AJPES)"
              />
              <text-input
                v-model="data[0].additional_names"
                name="additional_names"
                label="Druga imena, pod katerimi je organizacija poznana (kratice, okrajšave)"
              />
            </form-category>

            <form-category title="Kontakt">
              <text-input
                v-model="data[0].contact_name"
                name="contact_name"
                label="Ime in priimek"
              />
              <text-input v-model="data[0].contact_email" name="contact_email" label="E-naslov" />
              <text-input v-model="data[0].contact_phone" name="contact_phone" label="Telefon" />
            </form-category>

            <form-category title="Spletna prisotnost">
              <text-input v-model="data[0].web_page" name="web_page" label="URL spletne strani" />
              <template v-for="(social, i) in data[0].links">
                <text-input
                  :key="`social-links-${i}`"
                  v-model="social.url"
                  :name="`links__${i}`"
                  label="URL profila na družbenem mediju"
                />
              </template>
              <add-button
                text="Dodaj družbeni profil"
                @click.native="data[0].links.push({ url: null })"
              />
            </form-category>

            <form-category title="Slika">
              <file-input v-model="data[0].cover_photo" name="cover_photo" />
            </form-category>
          </template>

          <template v-else-if="activeStage === 1">
            <form-category title="Poslanstvo" note="največ 500 znakov">
              <text-input v-model="data[1].mission" name="mission" :multiline="9" />
            </form-category>

            <form-category title="Kratek opis" note="največ 1500 znakov">
              <text-input v-model="data[1].description" name="description" :multiline="27" />
            </form-category>

            <form-category title="Področja delovanja" note="lahko izberete več možnosti">
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="1"
                label="Človekove pravice, demokracija in enakost"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="2"
                label="Izobraževanje, raziskave in razvoj"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="3"
                label="Kultura"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="4"
                label="Mladina, otroci"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="5"
                label="Razvojno sodelovanje"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="6"
                label="Sociala"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="7"
                label="Šport"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="8"
                label="Okolje, narava in prostor"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="9"
                label="Zdravje"
              />
              <selection-option
                v-model="data[1].area"
                type="checkbox"
                name="area"
                value="10"
                label="Drugo (navedite kaj):"
              />
            </form-category>

            <form-category title="Proračun">
              <text-input
                v-model="data[1].avg_revenue"
                name="avg_revenue"
                label="Povprečni letni proračun v zadnjih treh letih"
              />
              <text-input
                v-model="data[1].employed"
                name="employed"
                label="Število zaposlenih v zadnjem zaključenem letu"
              />
            </form-category>

            <form-category title="Statusi">
              <selection-option
                v-model="data[1].is_charity"
                type="checkbox"
                name="is_charity"
                label="Organizacija ima status humanitarne organizacije"
              />
              <selection-option
                v-model="data[1].has_public_interest"
                type="checkbox"
                name="has_public_interest"
                label="Organizacija ima status delovanja v javnem interesu"
              />
              <selection-option
                v-model="data[1].is_voluntary"
                type="checkbox"
                name="is_voluntary"
                label="Organizacija je vpisana v evidenco prostotovoljskih organizacij"
              />
              <selection-option
                v-model="data[1].zero5"
                type="checkbox"
                name="zero5"
                label="Organizacija je na seznamu upravičencev do 0,5 % dohodnine"
              />
            </form-category>
          </template>

          <prev-next-buttons :page="activeStage" :pages="stages.length" @change="onChangeStage" />
        </form>
      </div>
    </div>
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
import PrevNextButtons from '~/components/PrevNextButtons.vue';

export default {
  components: {
    ContentTitle,
    FormStages,
    FormCategory,
    TextInput,
    SelectionOption,
    AddButton,
    FileInput,
    PrevNextButtons,
  },
  data() {
    return {
      stages: [
        {
          label: 'Osnovni podatki',
        },
        {
          label: 'Poslanstvo',
        },
        {
          label: 'Odbori',
        },
        {
          label: 'Finance',
        },
      ],
      activeStage: 1,
      data: [
        {
          name: null,
          additional_names: null,
          contact_name: null,
          contact_email: null,
          contact_phone: null,
          web_page: null,
          links: [{ url: null }],
          cover_photo: null,
        },
        {
          mission: null,
          description: null,
          area: [],
          avg_revenue: null,
          employed: null,
          is_charity: false,
          has_public_interest: false,
          is_voluntary: false,
          zero5: false,
        },
        {},
        {},
      ],
    };
  },
  methods: {
    onChangeStage(activeStage) {
      this.saveData(this.activeStage);

      this.activeStage = activeStage;

      const top = window.scrollY + this.$refs.formStages.$el.getBoundingClientRect().top - 48;
      this.$nextTick(() => {
        window.scrollTo(window.scrollX, top);
        const firstElem = this.$refs.form.querySelector(
          'button, input:not([type=image]), select, textarea',
        );
        if (firstElem) {
          firstElem.focus();
        }
      });
    },
    async saveData(stage) {
      const data = this.data[stage];
      const keys = Object.keys(data).filter((key) => data[key] != null);

      const jsonData = {};
      const formData = new FormData();
      // There's no way to inspect or iterate on FormData in IE
      let hasFormData = false;

      keys.forEach((key) => {
        let value = data[key];
        // Add http:// to links if missing!
        if (key === 'web_page') {
          const url = /^https?:\/\//.test(data[key]) ? data[key] : `http://${data[key]}`;
          value = url;
        }
        if (key === 'links') {
          const urls = data[key]
            .filter((e) => e.url)
            .map((e) => ({
              url: /^https?:\/\//.test(e.url) ? e.url : `http://${e.url}`,
            }));
          value = urls;
        }
        //

        if (value.file && value.file.name) {
          formData.append(key, value.file, value.file.name);
          hasFormData = true;
        } else {
          jsonData[key] = value;
        }
      });

      let method = 'post';
      let editKey = null;
      let id = null;
      if (Object.keys(jsonData).length > 0) {
        const jsonRes = await this.createOrUpdateOrg(method, jsonData, id, editKey);
        editKey = editKey || jsonRes.edit_key;
        id = id || jsonRes.id;
        method = 'patch';
      }
      if (hasFormData) {
        const formRes = await this.createOrUpdateOrg(method, formData, id, editKey);
        editKey = editKey || formRes.edit_key;
        id = id || formRes.id;
        method = 'patch';
      }
    },
    createOrUpdateOrg(method, data, id, editKey) {
      const query = `${editKey ? `?edit_key=${editKey}` : ''}`;
      const url = `/api/organizations/${id ? `${id}/` : ''}${query}`;
      return this.$axios[`$${method}`](url, data);
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

    @include media-breakpoint-down(sm) {
      margin-top: 2rem;
    }
  }
}
</style>
