<template>
  <div class="content">
    <content-title icon="signup-form" title="Prijava organizacije" />
    <div class="row justify-content-center">
      <div class="col-12 col-md-7 col-xxl-5">
        <form-stages
          ref="formStages"
          :stages="stages"
          :active="activeStage"
          @change="onChangeStage(false, $event)"
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
                :has-error="dataErrors.name"
              />
              <text-input
                v-model="data[0].additional_names"
                name="additional_names"
                label="Druga imena, pod katerimi je organizacija poznana (kratice, okrajšave)"
                :has-error="dataErrors.additional_names"
              />
            </form-category>

            <form-category title="Kontakt">
              <text-input
                v-model="data[0].contact_name"
                name="contact_name"
                label="Ime in priimek"
                :has-error="dataErrors.contact_name"
              />
              <text-input
                v-model="data[0].contact_email"
                name="contact_email"
                label="E-naslov"
                :has-error="dataErrors.contact_email"
              />
              <text-input
                v-model="data[0].contact_phone"
                name="contact_phone"
                label="Telefon"
                :has-error="dataErrors.contact_phone"
              />
            </form-category>

            <form-category title="Spletna prisotnost">
              <text-input
                v-model="data[0].web_page"
                name="web_page"
                label="URL spletne strani"
                :has-error="dataErrors.web_page"
              />
              <template v-for="(link, i) in data[0].links">
                <text-input
                  :key="`link-${i}`"
                  v-model="link.url"
                  :name="`links__${i}`"
                  label="URL profila na družbenem mediju"
                  :has-error="dataErrors.links && dataErrors.links[i]"
                />
              </template>
              <add-button
                text="Dodaj družbeni profil"
                @click.native="data[0].links.push({ url: null })"
              />
            </form-category>

            <form-category title="Slika">
              <file-input
                v-model="data[0].cover_photo"
                name="cover_photo"
                :has-error="dataErrors.cover_photo"
              />
            </form-category>

            <form-category title="Davčna številka">
              <text-input
                v-model="data[0].tax_number"
                name="tax_number"
                label="Davčna številka"
                :has-error="dataErrors.tax_number"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 1">
            <form-category title="Poslanstvo" note="največ 500 znakov">
              <text-input
                v-model="data[1].mission"
                name="mission"
                :multiline="9"
                :has-error="dataErrors.mission"
              />
            </form-category>

            <form-category title="Kratek opis" note="največ 1500 znakov">
              <text-input
                v-model="data[1].description"
                name="description"
                :multiline="27"
                :has-error="dataErrors.description"
              />
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
                :has-error="dataErrors.avg_revenue"
              />
              <text-input
                v-model="data[1].employed"
                name="employed"
                label="Število zaposlenih v zadnjem zaključenem letu"
                :has-error="dataErrors.employed"
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

          <template v-else-if="activeStage === 2">
            <form-category title="Zapisniki seje">
              <selection-option
                v-model="data[2].has_minutes_meeting"
                type="checkbox"
                name="has_minutes_meeting"
                label="Organizacija vodi zapisnike sej"
              />
              <file-input
                v-if="data[2].has_minutes_meeting"
                v-model="data[2].minutes_meeting"
                name="minutes_meeting"
                label="Priložite zapisnik zadnje seje"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 3">
            <form-category title="Strateško načrtovanje">
              <selection-option
                v-model="data[3].strategic_planning"
                type="checkbox"
                name="strategic_planning"
                label="Organizacija strateško načrtuje"
              />
              <div v-if="data[3].strategic_planning">
                <selection-option
                  v-model="data[3].has_milestiones_description"
                  type="checkbox"
                  name="has_milestiones_description"
                  label="Organizacija spremlja doseganje strateških ciljev"
                />
                <text-input
                  v-if="data[3].has_milestiones_description"
                  v-model="data[3].milestiones_description"
                  name="milestiones_description"
                  label="Kratek opis kako (največ 500 znakov)"
                  :multiline="9"
                  :has-error="dataErrors.milestiones_description"
                />

                <selection-option
                  v-model="data[3].has_strategic_goals"
                  type="checkbox"
                  name="has_strategic_goals"
                  label="Organizacija vodi pisna poročila o spremljanju stateških ciljev"
                />
                <file-input
                  v-if="data[3].has_strategic_goals"
                  v-model="data[3].strategic_goals"
                  name="strategic_goals"
                  label="Priložite poročilo"
                  :has-error="dataErrors.strategic_goals"
                />
              </div>
            </form-category>

            <form-category title="Finančno poročilo">
              <p>
                Finančno poročilo pripravljeno po
                <a
                  :href="`${apiBaseUrl}/documents/1/vzorec_finan%C4%8Dnega_poro%C4%8Dila.xlsx`"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <span>vzorcu finančnega poročila</span>
                </a>
                .
              </p>
              <file-input
                v-model="data[3].finance_report"
                name="finance_report"
                label="Priložite finančno poročilo"
              />
            </form-category>

            <form-category title="Finančno poročilo, ki je bilo oddano na AJPES">
              <file-input
                v-model="data[3].finance_report_ajpes"
                name="finance_report_ajpes"
                label="Priložite finančno poročilo"
              />
            </form-category>

            <form-category title="Revidiranje finančnega poročila">
              <selection-option
                v-model="data[3].has_audited_report"
                type="checkbox"
                name="has_audited_report"
                label="Organizacija je dolžna revidirati svoja finančna poročila"
              />
              <file-input
                v-if="data[3].has_audited_report"
                v-model="data[3].audited_report"
                name="audited_report"
                label="Priložite revidirano poročilo"
              />
            </form-category>

            <form-category title="Finančni načrt">
              <selection-option
                v-model="data[3].has_finance_plan"
                type="checkbox"
                name="has_finance_plan"
                label="Organizacija ima finančni načrt za tekoče leto"
              />
              <file-input
                v-if="data[3].has_finance_plan"
                v-model="data[3].finance_plan"
                name="finance_plan"
                label="Priložite finančni načrt"
              />
            </form-category>

            <form-category title="Posojila">
              <selection-option
                v-model="data[3].has_given_loan"
                type="checkbox"
                name="has_given_loan"
                label="Organizacija daje posojila povezanim osebam (zaposleni, člani upravnega/nadzornega odbora in njihovi družinski člani, ...)"
              />
              <file-input
                v-if="data[3].has_given_loan"
                v-model="data[3].given_loan"
                name="given_loan"
                label="Priložite seznam danih posojil"
              />

              <selection-option
                v-model="data[3].has_received_loans"
                type="checkbox"
                name="has_received_loans"
                label="Organizacija prejema posojila od povezanih oseb (zaposleni, člani upravnega/nadzornega odbora in njihovi družinski člani, ...)"
              />
              <file-input
                v-if="data[3].has_received_loans"
                v-model="data[3].received_loans"
                name="received_loans"
                label="Priložite seznam prejetih posojil"
              />
            </form-category>

            <form-category title="Plačilni razredi">
              <selection-option
                v-model="data[3].has_payment_classes"
                type="checkbox"
                name="has_payment_classes"
                label="Organizacija ima akt o sistematizaciji delovnih mest in plačnih razredov"
              />
              <file-input
                v-if="data[3].has_payment_classes"
                v-model="data[3].payment_classes"
                name="payment_classes"
                label="Priložite akt"
              />

              <text-input
                v-model="data[3].wages_ratio"
                name="wages_ratio"
                label="Razmerje med najvišjo in povprečno plačo v organizaciji"
                :has-error="dataErrors.wages_ratio"
              />
            </form-category>
          </template>

          <prev-next-buttons
            :page="activeStage"
            :pages="stages.length"
            @change="onChangeStage(true, $event)"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { isEqual, cloneDeep } from 'lodash';
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
      apiBaseUrl: process.env.API_BASE_URL,
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
      activeStage: 0,
    };
  },
  async asyncData({ $axios, query, error }) {
    const editId = query.edit_id || null;
    const editKey = query.edit_key || null;

    let initialData = {};
    if (editId && editKey) {
      initialData = await $axios.$get(`/api/organizations/${editId}/?edit_key=${editKey}`);
    }

    const data = [
      {
        name: initialData.name || '',
        additional_names: initialData.additional_names || '',
        contact_name: initialData.contact_name || '',
        contact_email: initialData.contact_email || '',
        contact_phone: initialData.contact_phone || '',
        web_page: initialData.web_page || '',
        links:
          initialData.links && initialData.links.length
            ? cloneDeep(initialData.links)
            : [{ url: '' }],
        cover_photo: initialData.cover_photo || null,
        tax_number: initialData.tax_number || '',
      },
      {
        mission: initialData.mission || '',
        description: initialData.description || '',
        area: initialData.area ? initialData.area.slice() : [],
        avg_revenue: initialData.avg_revenue || '',
        employed: initialData.employed || 0,
        is_charity: initialData.is_charity || false,
        has_public_interest: initialData.has_public_interest || false,
        is_voluntary: initialData.is_voluntary || false,
        zero5: initialData.zero5 || false,
      },
      {
        has_minutes_meeting: initialData.has_minutes_meeting || false,
        minutes_meeting: initialData.minutes_meeting || null,
      },
      {
        strategic_planning: initialData.strategic_planning || false,
        has_milestiones_description: initialData.has_milestiones_description || false,
        milestiones_description: initialData.milestiones_description || '',
        has_strategic_goals: initialData.has_strategic_goals || false,
        strategic_goals: initialData.strategic_goals || null,
        finance_report: initialData.finance_report || null,
        finance_report_ajpes: initialData.finance_report_ajpes || null,
        has_audited_report: initialData.has_audited_report || false,
        audited_report: initialData.audited_report || null,
        has_finance_plan: initialData.has_finance_plan || false,
        finance_plan: initialData.finance_plan || null,
        has_given_loans: initialData.has_given_loans || false,
        given_loans: initialData.given_loans || null,
        has_received_loans: initialData.has_received_loans || false,
        received_loans: initialData.received_loans || null,
        has_payment_classes: initialData.has_payment_classes || false,
        payment_classes: initialData.payment_classes || null,
        wages_ratio: initialData.wages_ratio || '',
      },
    ];

    return {
      editId,
      editKey,
      initialData,
      data,
      dataErrors: {},
    };
  },
  methods: {
    async onChangeStage(save, activeStage) {
      if (save) {
        const saved = await this.saveData(this.activeStage);
        if (saved) {
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
        }
      } else {
        this.activeStage = activeStage;
      }
    },
    async saveData(stage) {
      this.saving = true;

      const data = this.data[stage];
      const keys = Object.keys(data).filter((key) => {
        return !isEqual(data[key], this.initialData[key]);
      });

      const jsonData = {};
      const formData = new FormData();
      // There's no way to inspect or iterate on FormData in IE
      let hasFormData = false;

      keys.forEach((key) => {
        // Add http:// to links if missing!
        if (key === 'web_page') {
          const url = /^https?:\/\//.test(data[key]) ? data[key] : `http://${data[key]}`;
          data[key] = url;
        }
        if (key === 'links') {
          const urls = data[key]
            .filter((e) => e.url)
            .map((e) => ({
              url: /^https?:\/\//.test(e.url) ? e.url : `http://${e.url}`,
            }));
          data[key] = urls;
        }
        //
        const value = data[key];

        if (value && value.file && value.file.name) {
          formData.append(key, value.file, value.file.name);
          hasFormData = true;
        } else {
          jsonData[key] = value;
        }
      });

      try {
        if (Object.keys(jsonData).length > 0) {
          await this.createOrUpdateOrg(jsonData);
        }
        if (hasFormData) {
          await this.createOrUpdateOrg(formData);
        }
      } catch (error) {
        // eslint-disable-next-line no-console
        console.dir(error);

        if (error.response && error.response.data) {
          let focusedFirst = false;
          Object.keys(error.response.data).forEach((key) => {
            this.$set(this.dataErrors, key, error.response.data[key].join(', '));
            if (!focusedFirst) {
              const el = this.$refs.form.querySelector(`[name="${key}"]`);
              if (el) {
                el.focus();
                focusedFirst = true;
              }
            }
          });
        } else {
          alert(error.message);
        }

        return false;
      }

      this.saving = false;
      return true;
    },
    async createOrUpdateOrg(data) {
      const method = this.editId && this.editKey ? 'patch' : 'post';
      const query = `${this.editKey ? `?edit_key=${this.editKey}` : ''}`;
      const url = `/api/organizations/${this.editId ? `${this.editId}/` : ''}${query}`;
      const res = await this.$axios[`$${method}`](url, data);
      if ((!this.editId || !this.editKey) && res.id && res.edit_key) {
        this.editId = res.id;
        this.editKey = res.edit_key;
        this.$router.replace({
          query: {
            edit_id: this.editId,
            edit_key: this.editKey,
          },
        });
      }
      this.initialData = res;
      return res;
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

    legend + p {
      margin-top: -1.5rem;
    }
  }
}
</style>
