<template>
  <div class="content">
    <content-title icon="signup-form" title="Prijava organizacije" />
    <div class="row justify-content-center">
      <div class="col-12 col-md-9 col-xxl-7">
        <form-stages
          ref="formStages"
          :stages="stages"
          :active="activeStage"
          @change="onChangeStage(false, $event)"
        />
      </div>
    </div>
    <div class="row justify-content-center form-row">
      <div class="col-12 col-md-8 col-xxl-6">
        <form ref="form" @submit.prevent>
          <template v-if="activeStage === -1">
            <p class="lead text-justify">
              Veseli nas, da ste se odločili vpisati vašo organizacijo na
              spletno stran <em>dobrodelen.si</em> in širši javnosti pokazati,
              kako transparenti in odgovorni ste pri svojem poslovanju.
            </p>
            <p class="lead text-justify">
              Preden začnete z vpisovanjem podatkov o svoji organizaciji
              podrobno preberite
              <a
                :href="`${apiBaseUrl}/TODO_LINK.pdf`"
                target="_blank"
                rel="noopener noreferrer"
                >METODOLOGIJA ZA PREGLED TRANSPARENTOSTI SLOVENSKIH NEVLADNIH
                ORGANIZACIJ</a
              >.
            </p>
            <p class="lead text-justify">
              V njej so predstavljeni sklopi pregleda s kriteriji in pogoji
              njihovega izpolnjevanja. Glede na število izpolnjenih kriterijev
              bodo organizaciji dodeljene zvezdice, ki bodo odražale njeno
              transparentnost. Več zvezdic organizacija doseže, bolj
              transparentna je v svojem delovanju.
            </p>
          </template>

          <template v-if="activeStage >= 0 && activeStage < stages.length">
            <p class="lead text-justify above-form-info-text">
              Navodila za pregled doseganja kriterijev so dostopna v Prilogi 1
              <a
                :href="`${apiBaseUrl}/TODO_LINK.pdf`"
                target="_blank"
                rel="noopener noreferrer"
                >Metodologije za pregled transparentnosti slovenskih nevladnih
                organizacij</a
              >
            </p>
          </template>

          <template v-if="activeStage === 0">
            <form-category title="Naziv organizacije">
              <text-input
                v-model="data[activeStage].name"
                name="name"
                label="Uradno ime organizacije (iz AJPES)"
                :has-error="dataErrors.name"
              />
              <text-input
                v-model="data[activeStage].additional_names"
                name="additional_names"
                label="Druga imena, pod katerimi je organizacija poznana (kratice, okrajšave)"
                :has-error="dataErrors.additional_names"
              />
            </form-category>

            <form-category title="Slika">
              <file-input
                v-model="data[activeStage].cover_photo"
                name="cover_photo"
                label="Naložite sliko"
                :has-error="dataErrors.cover_photo"
              />
            </form-category>

            <form-category title="Naslov">
              <text-input
                v-model="data[activeStage].address"
                name="address"
                label="Naslov organizacije"
                :has-error="dataErrors.address"
              />
            </form-category>

            <form-category title="Kontakt">
              <text-input
                v-model="data[activeStage].contact_name"
                name="contact_name"
                label="Ime in priimek"
                :has-error="dataErrors.contact_name"
              />
              <text-input
                v-model="data[activeStage].contact_email"
                name="contact_email"
                label="E-naslov"
                :has-error="dataErrors.contact_email"
              />
              <text-input
                v-model="data[activeStage].contact_phone"
                name="contact_phone"
                label="Telefon"
                :has-error="dataErrors.contact_phone"
              />
            </form-category>

            <form-category title="Davčna številka">
              <text-input
                v-model="data[activeStage].tax_number"
                name="tax_number"
                label="Davčna številka"
                :has-error="dataErrors.tax_number"
              />
            </form-category>

            <form-category title="Spletna prisotnost">
              <text-input
                v-model="data[activeStage].web_page"
                name="web_page"
                label="URL spletne strani"
                :has-error="dataErrors.web_page"
              />
              <template
                v-for="(link, i) in data[activeStage].links"
                :key="`link-${i}`"
              >
                <text-input
                  v-model="link.url"
                  :name="`links__${i}`"
                  label="URL profila na družbenem mediju"
                  :has-error="dataErrors.links && dataErrors.links[i]"
                />
              </template>
              <button
                v-if="data[activeStage].links.length"
                type="button"
                class="btn btn-link remove-member"
                @click="data[activeStage].links.pop()"
              >
                <span>&times;</span> Odstrani družbeni profil
              </button>
              <add-button
                text="Dodajte družbeni profil"
                @click.native="data[activeStage].links.push({ url: null })"
              />
            </form-category>

            <form-category
              title="Regija delovanja organizacije"
              note="lahko izberete več možnosti"
            >
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                label="Vsa"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="1"
                label="Gorenjska"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="2"
                label="Goriška"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="3"
                label="Jugovzhodna Slovenija"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="4"
                label="Koroška"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="5"
                label="Notranjskokraška"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="6"
                label="Obalnokraška"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="7"
                label="Osrednjeslovenska"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="8"
                label="Podravska"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="9"
                label="Pomurska"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="10"
                label="Posavska"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="11"
                label="Savinjska"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="12"
                label="Zasavska"
              />
            </form-category>

            <form-category
              title="Področja delovanja"
              note="lahko izberete več možnosti"
            >
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="1"
                label="Človekove pravice, demokracija in enakost"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="2"
                label="Izobraževanje, raziskave in razvoj"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="3"
                label="Kultura"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="4"
                label="Mladina, otroci"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="5"
                label="Razvojno sodelovanje"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="6"
                label="Sociala"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="7"
                label="Šport"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="8"
                label="Okolje, narava in prostor"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="9"
                label="Zdravje"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="11"
                label="Starejši"
              />
              <selection-option
                v-model="data[activeStage].area"
                type="checkbox"
                name="area"
                :value="10"
                label="Drugo:"
                custom-input
                :custom-input-value="data[activeStage].custom_area"
                @custom-change="data[activeStage].custom_area = $event"
              />
            </form-category>

            <!-- <form-category title="Donacije">
              <text-input
                v-model="data[activeStage].account_number"
                name="account_number"
                label="Številka tekočega računa"
                :has-error="dataErrors.account_number"
              />
              <text-input
                v-model="data[activeStage].donation_url"
                name="donation_url"
                label="Povezava na spletno stran organizacije, kjer je možno donirati sredstva (če obstaja)"
                :has-error="dataErrors.donation_url"
              />
            </form-category> -->

            <!-- <form-category title="Proračun">
              <text-input
                v-model="data[activeStage].avg_revenue"
                name="avg_revenue"
                label="Povprečni letni proračun v zadnjem letu"
                :has-error="dataErrors.avg_revenue"
              />
              <text-input
                v-model="data[activeStage].employed"
                name="employed"
                label="Število zaposlenih v zadnjem zaključenem letu"
                :has-error="dataErrors.employed"
              />
            </form-category> -->

            <!-- <form-category title="Statusi">
              <selection-option
                v-model="data[activeStage].is_charity"
                type="checkbox"
                name="is_charity"
                label="Organizacija ima status humanitarne organizacije"
              />
              <selection-option
                v-model="data[activeStage].has_public_interest"
                type="checkbox"
                name="has_public_interest"
                label="Organizacija ima status delovanja v javnem interesu"
              />
              <selection-option
                v-model="data[activeStage].is_voluntary"
                type="checkbox"
                name="is_voluntary"
                label="Organizacija je vpisana v evidenco prostovoljskih organizacij"
              />
              <selection-option
                v-model="data[activeStage].zero5"
                type="checkbox"
                name="zero5"
                label="Organizacija je na seznamu upravičencev do 1 % dohodnine"
              />
              <text-input
                v-if="data[activeStage].zero5"
                v-model="data[activeStage].zero5_amount"
                name="zero5_amount"
                label="Višina zbranih sredstev prek 1 % dohodnine"
                :has-error="dataErrors.zero5_amount"
              />
            </form-category> -->
          </template>

          <template v-else-if="activeStage === 1">
            <!-- SKLOP 1 Kriteriji -->
            <form-category title="Sklop 1: Kriteriji">
              <selection-option
                v-model="data[activeStage].has_published_key_documents"
                type="checkbox"
                name="has_published_key_documents"
                label="Kriterij 1: Organizacija ima objavljene ključne dokumente (akt o ustanovitvi in/ali statut)"
              />
              <text-input
                v-if="data[activeStage].has_published_key_documents"
                v-model="data[activeStage].key_documents_url"
                name="key_documents_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.key_documents_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_mission"
                type="checkbox"
                name="has_published_mission"
                label="Kriterij 2: Organizacija ima objavljeno poslanstvo"
              />
              <text-input
                v-if="data[activeStage].has_published_mission"
                v-model="data[activeStage].mission_url"
                name="mission_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.mission_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_key_employee_list"
                type="checkbox"
                name="has_published_key_employee_list"
                label="Kriterij 3: Organizacija ima objavljen seznam ključnih zaposlenih"
              />
              <text-input
                v-if="data[activeStage].has_published_key_employee_list"
                v-model="data[activeStage].key_employee_list_url"
                name="key_employee_list_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.key_employee_list_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_board_member_list"
                type="checkbox"
                name="has_published_board_member_list"
                label="Kriterij 4: Organizacija ima objavljen seznam članov nadzornih organov"
              />
              <text-input
                v-if="data[activeStage].has_published_board_member_list"
                v-model="data[activeStage].board_member_list_url"
                name="board_member_list_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.board_member_list_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_contact_information"
                type="checkbox"
                name="has_published_contact_information"
                label="Kriterij 5: Objavljen je način, kako lahko posameznik stopi v stik z organizacijo"
              />
              <text-input
                v-if="data[activeStage].has_published_contact_information"
                v-model="data[activeStage].contact_information_url"
                name="contact_information_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.contact_information_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_complaints_contact"
                type="checkbox"
                name="has_published_complaints_contact"
                label="Kriterij 6: Objavljene so informacije o možnosti pritožbe nad delom organizacije s podatki komu/kako poslati pritožbe"
              />
              <text-input
                v-if="data[activeStage].has_published_complaints_contact"
                v-model="data[activeStage].complaints_contact_url"
                name="complaints_contact_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.complaints_contact_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_complaints_process"
                type="checkbox"
                name="has_published_complaints_process"
                label="Kriterij 7: Objavljen je celoten pritožbeni postopek"
              />
              <text-input
                v-if="data[activeStage].has_published_complaints_process"
                v-model="data[activeStage].complaints_process_url"
                name="complaints_process_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.complaints_process_url"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 2">
            <!-- SKLOP 2 Kriteriji -->
            <form-category title="Sklop 2: Kriteriji">
              <selection-option
                v-model="data[activeStage].has_published_substantive_report"
                type="checkbox"
                name="has_published_substantive_report"
                label="Kriterij 1: Objavljeno je vsebinsko poročilo za preteklo leto"
              />
              <text-input
                v-if="data[activeStage].has_published_substantive_report"
                v-model="data[activeStage].substantive_report_url"
                name="substantive_report_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.substantive_report_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_report_about_work"
                type="checkbox"
                name="has_published_report_about_work"
                label="Kriterij 2: Objavljeno je vsebinsko poročilo, iz katerega je jasno razvidno, s čim se organizacija ukvarja"
              />
              <text-input
                v-if="data[activeStage].has_published_report_about_work"
                v-model="data[activeStage].report_about_work_url"
                name="report_about_work_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.report_about_work_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_report_with_results"
                type="checkbox"
                name="has_published_report_with_results"
                label="Kriterij 3: Vsebinsko poročilo vključuje tudi rezultate (dosežke, učinke), ne zgolj aktivnosti"
              />
              <text-input
                v-if="data[activeStage].has_published_report_with_results"
                v-model="data[activeStage].report_with_results_url"
                name="report_with_results_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.report_with_results_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_work_plan"
                type="checkbox"
                name="has_published_work_plan"
                label="Kriterij 4: Organizacija ima objavljen načrt dela za tekoče leto"
              />
              <text-input
                v-if="data[activeStage].has_published_work_plan"
                v-model="data[activeStage].work_plan_url"
                name="work_plan_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.work_plan_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_strategic_objectives"
                type="checkbox"
                name="has_published_strategic_objectives"
                label="Kriterij 5: Organizacija ima objavljene glavne strateške cilje"
              />
              <text-input
                v-if="data[activeStage].has_published_strategic_objectives"
                v-model="data[activeStage].strategic_objectives_url"
                name="strategic_objectives_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.strategic_objectives_url"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 3">
            <!-- SKLOP 3 Kriteriji -->
            <form-category title="Sklop 3: Kriteriji">
              <selection-option
                v-model="data[activeStage].has_published_financial_report"
                type="checkbox"
                name="has_published_financial_report"
                label="Kriterij 1: Organizacija ima objavljeno letno finančno poročilo za preteklo leto"
              />
              <text-input
                v-if="data[activeStage].has_published_financial_report"
                v-model="data[activeStage].financial_report_url"
                name="financial_report_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.financial_report_url"
              />

              <selection-option
                v-model="
                  data[activeStage]
                    .has_published_understandable_financial_report
                "
                type="checkbox"
                name="has_published_understandable_financial_report"
                label="Kriterij 2: Finančna poročila so razdeljena po vrstah stroškov, ki so razumljiva javnosti (npr. stroški zaposlenih, potni stroški, stroški za zunanje izvajalce, itd.)"
              />
              <text-input
                v-if="
                  data[activeStage]
                    .has_published_understandable_financial_report
                "
                v-model="data[activeStage].understandable_financial_report_url"
                name="understandable_financial_report_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.understandable_financial_report_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_operating_expenses"
                type="checkbox"
                name="has_published_operating_expenses"
                label="Kriterij 3: Objavljen je podatek o višini ali odstotku sredstev, ki ga organizacija nameni za delovanje (hladni pogon)"
              />
              <text-input
                v-if="data[activeStage].has_published_operating_expenses"
                v-model="data[activeStage].operating_expenses_url"
                name="operating_expenses_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.operating_expenses_url"
              />

              <selection-option
                v-model="
                  data[activeStage].has_published_main_sources_of_financing
                "
                type="checkbox"
                name="has_published_main_sources_of_financing"
                label="Kriterij 4: Objavljeni so glavni viri financiranja (prihodki)"
              />
              <text-input
                v-if="data[activeStage].has_published_main_sources_of_financing"
                v-model="data[activeStage].main_sources_of_financing_url"
                name="main_sources_of_financing_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.main_sources_of_financing_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_management_revenues"
                type="checkbox"
                name="has_published_management_revenues"
                label="Kriterij 5: Objavljeni so prihodki vodstva"
              />
              <text-input
                v-if="data[activeStage].has_published_management_revenues"
                v-model="data[activeStage].management_revenues_url"
                name="management_revenues_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.management_revenues_url"
              />

              <selection-option
                v-model="data[activeStage].has_published_salary_ratio"
                type="checkbox"
                name="has_published_salary_ratio"
                label="Kriterij 6: Objavljeno je razmerje med najnižjo, povprečno in najvišjo plačo"
              />
              <text-input
                v-if="data[activeStage].has_published_salary_ratio"
                v-model="data[activeStage].salary_ratio_url"
                name="salary_ratio_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.salary_ratio_url"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 4">
            <!-- SKLOP 4 Kriteriji -->
            <form-category title="Sklop 4: Kriteriji">
              <selection-option
                v-model="data[activeStage].has_published_fundraising_reports"
                type="checkbox"
                name="has_published_fundraising_reports"
                label="Kriterij 1: Objavljena so poročila o zbranih sredstvih"
              />
              <text-input
                v-if="data[activeStage].has_published_fundraising_reports"
                v-model="data[activeStage].fundraising_reports_url"
                name="fundraising_reports_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.fundraising_reports_url"
              />

              <selection-option
                v-model="
                  data[activeStage]
                    .has_published_fundraising_report_with_purposes
                "
                type="checkbox"
                name="has_published_fundraising_report_with_purposes"
                label="Kriterij 2: Poročilo o zbranih sredstvih je razdeljeno po namenih zbiranja (fundraising akcijah)"
              />
              <text-input
                v-if="
                  data[activeStage]
                    .has_published_fundraising_report_with_purposes
                "
                v-model="data[activeStage].fundraising_report_with_purposes_url"
                name="fundraising_report_with_purposes_url"
                label="URL do objavljenega dokumenta/podatkov"
                :has-error="dataErrors.fundraising_report_with_purposes_url"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 5">
            <!-- SKLOP 5 Kriteriji -->
            <form-category title="Sklop 5: Kriteriji">
              <selection-option
                v-model="data[activeStage].website_accessibility_contrast"
                type="checkbox"
                name="website_accessibility_contrast"
                label="Kriterij 1: Barvni kontrast med tekstom in ozadjem spletne strani je vsaj 4.5:1"
              />
              <selection-option
                v-model="data[activeStage].website_accessibility_zoom"
                type="checkbox"
                name="website_accessibility_zoom"
                label="Kriterij 2: Spletno mesto je berljivo tudi ob povečavi na 200 %"
              />
              <selection-option
                v-model="data[activeStage].website_accessibility_disabilities"
                type="checkbox"
                name="website_accessibility_disabilities"
                label="Kriterij 3: Spletna stran je dostopna osebam z motoričnimi ali kognitivnimi ovirami"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === stages.length">
            <h4>Prijava je bila uspešna!</h4>
            <p>Za ponovno urejanje podatkov, si shranite ta url:</p>
            <code>{{ getWindowLocation() }}</code>
          </template>

          <prev-next-buttons
            :page="activeStage"
            :pages="stages.length"
            :disabled="saving"
            @change="onChangeStage"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
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
  async setup() {
    const config = useRuntimeConfig();
    const route = useRoute();

    const editId = route.query.edit_id;
    const editKey = route.query.edit_key;

    const { data: initialData } = await useAsyncData('initialData', () => {
      if (editId && editKey) {
        const apiBase = process.server
          ? config.public.apiBaseServer
          : config.public.apiBase;
        return $fetch(
          `${apiBase}/api/organizations/${editId}/?edit_key=${editKey}`,
        );
      }
      return {};
    });

    return {
      apiBaseUrl: config.public.apiBase,
      editId,
      editKey,
      initialData,
    };
  },
  data() {
    const init = this.initialData;

    const data = [
      // OSEBNA IZKAZNICA ORGANIZACIJE
      {
        name: init.name || '',
        additional_names: init.additional_names || '',
        cover_photo: init.cover_photo || null,
        address: init.address || '',
        contact_name: init.contact_name || '',
        contact_email: init.contact_email || '',
        contact_phone: init.contact_phone || '',
        tax_number: init.tax_number || '',
        web_page: init.web_page || '',
        links:
          init.links && init.links.length
            ? _.cloneDeep(init.links)
            : [{ url: '' }],
        region: init.region ? init.region.slice() : [],
        area: init.area ? init.area.slice() : [],
        custom_area: init.custom_area || '',
      },
      // DOSTOPNOST OSNOVNIH INFORMACIJ
      {
        has_published_key_documents: init.has_published_key_documents || false,
        key_documents_url: init.key_documents_url || '',
        has_published_mission: init.has_published_mission || false,
        mission_url: init.mission_url || '',
        has_published_key_employee_list:
          init.has_published_key_employee_list || false,
        key_employee_list_url: init.key_employee_list_url || '',
        has_published_board_member_list:
          init.has_published_board_member_list || false,
        board_member_list_url: init.board_member_list_url || '',
        has_published_contact_information:
          init.has_published_contact_information || false,
        contact_information_url: init.contact_information_url || '',
        has_published_complaints_contact:
          init.has_published_complaints_contact || false,
        complaints_contact_url: init.complaints_contact_url || '',
        has_published_complaints_process:
          init.has_published_complaints_process || false,
        complaints_process_url: init.complaints_process_url || '',
      },
      // DOSTOPNOST VSEBINSKIH POROČIL
      {
        has_published_substantive_report:
          init.has_published_substantive_report || false,
        substantive_report_url: init.substantive_report_url || '',
        has_published_report_about_work:
          init.has_published_report_about_work || false,
        report_about_work_url: init.report_about_work_url || '',
        has_published_report_with_results:
          init.has_published_report_with_results || false,
        report_with_results_url: init.report_with_results_url || '',
        has_published_work_plan: init.has_published_work_plan || false,
        work_plan_url: init.work_plan_url || '',
        has_published_strategic_objectives:
          init.has_published_strategic_objectives || false,
        strategic_objectives_url: init.strategic_objectives_url || '',
      },
      // FINANČNA TRANSPARENTNOST
      {
        has_published_financial_report:
          init.has_published_financial_report || false,
        financial_report_url: init.financial_report_url || '',
        has_published_understandable_financial_report:
          init.has_published_understandable_financial_report || false,
        understandable_financial_report_url:
          init.understandable_financial_report_url || '',
        has_published_operating_expenses:
          init.has_published_operating_expenses || false,
        operating_expenses_url: init.operating_expenses_url || '',
        has_published_main_sources_of_financing:
          init.has_published_main_sources_of_financing || false,
        main_sources_of_financing_url: init.main_sources_of_financing_url || '',
        has_published_management_revenues:
          init.has_published_management_revenues || false,
        management_revenues_url: init.management_revenues_url || '',
        has_published_salary_ratio: init.has_published_salary_ratio || false,
        salary_ratio_url: init.salary_ratio_url || '',
      },
      // ZBIRANJE DONACIJSKIH SREDSTEV
      {
        has_published_fundraising_reports:
          init.has_published_fundraising_reports || false,
        fundraising_reports_url: init.fundraising_reports_url || '',
        has_published_fundraising_report_with_purposes:
          init.has_published_fundraising_report_with_purposes || false,
        fundraising_report_with_purposes_url:
          init.fundraising_report_with_purposes_url || '',
      },
      // DOSTOP OBJAVLJENIH INFORMACIJ
      {
        website_accessibility_contrast:
          init.website_accessibility_contrast || false,
        website_accessibility_zoom: init.website_accessibility_zoom || false,
        website_accessibility_disabilities:
          init.website_accessibility_disabilities || false,
      },
    ];

    return {
      stages: [
        { label: 'OSEBNA IZKAZNICA ORGANIZACIJE' },
        { label: 'DOSTOPNOST OSNOVNIH INFORMACIJ' },
        { label: 'DOSTOPNOST VSEBINSKIH POROČIL' },
        { label: 'FINANČNA TRANSPARENTNOST' },
        { label: 'ZBIRANJE DONACIJSKIH SREDSTEV' },
        { label: 'DOSTOP OBJAVLJENIH INFORMACIJ' },
      ],
      activeStage: -1,
      data,
      dataErrors: {},
      saving: false,
    };
  },
  methods: {
    async onChangeStage(save, activeStage) {
      if (save) {
        const saved = await this.saveData(this.activeStage);
        if (saved) {
          this.activeStage = activeStage;

          const top =
            window.scrollY +
            this.$refs.formStages.$el.getBoundingClientRect().top -
            48;
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
      if (data) {
        // Delete custom area if not selected
        if (data.area && data.area.filter((e) => e === 10).length === 0) {
          data.custom_area = '';
        }

        const keys = Object.keys(data).filter((key) => {
          return !_.isEqual(data[key], this.initialData[key]);
        });

        const jsonData = {};
        const formData = new FormData();
        // There's no way to inspect or iterate on FormData in IE
        let hasFormData = false;

        keys.forEach((key) => {
          // Add http:// to links if missing!
          if (key === 'web_page' || key.endsWith('_url')) {
            if (data[key]) {
              const url = /^https?:\/\//.test(data[key])
                ? data[key]
                : `http://${data[key]}`;
              data[key] = url;
            }
          }
          if (key === 'links') {
            const urls = data[key]
              .filter((e) => e.url)
              .map((e) => ({
                url: /^https?:\/\//.test(e.url) ? e.url : `http://${e.url}`,
              }));
            data[key] = urls;
          }
          const value = data[key];

          if (value && value.file && value.file.name) {
            formData.append(key, value.file, value.file.name);
            hasFormData = true;
          } else {
            jsonData[key] = value;
          }
        });

        if (stage === this.data.length - 1) {
          // last stage
          jsonData.is_complete = true;
        }

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
              if (Array.isArray(error.response.data[key]) && key !== 'detail') {
                this.$set(
                  this.dataErrors,
                  key,
                  error.response.data[key].join(', '),
                );
                if (!focusedFirst) {
                  const el = this.$refs.form.querySelector(`[name="${key}"]`);
                  if (el) {
                    el.focus();
                    focusedFirst = true;
                  }
                }
              } else {
                alert(key + ': ' + String(error.response.data[key]));
              }
            });
          } else {
            alert(error.message);
          }

          this.saving = false;
          return false;
        }
      }

      this.saving = false;
      return true;
    },
    async createOrUpdateOrg(data) {
      const method = this.editId && this.editKey ? 'PATCH' : 'POST';
      const query = `${this.editKey ? `?edit_key=${this.editKey}` : ''}`;
      const url = `${this.apiBaseUrl}/api/organizations/${
        this.editId ? `${this.editId}/` : ''
      }${query}`;
      const res = await $fetch(url, { method, body: data });
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
    getWindowLocation() {
      return typeof window !== 'undefined' ? window.location.href : '';
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
  em {
    // font-weight: 400;
    // font-style: italic;
    font-style: normal;
  }

  .form-row {
    margin-top: 4rem;

    @include media-breakpoint-down(sm) {
      margin-top: 2rem;
    }

    p.above-form-info-text {
      margin-bottom: 4rem;

      @include media-breakpoint-down(sm) {
        margin-bottom: 2rem;
      }
    }

    legend + p {
      margin-top: -1.5rem;
    }

    fieldset h4 {
      font-weight: 300;
      // letter-spacing: 0.2em;
      font-size: 1.5rem;

      @include media-breakpoint-down(sm) {
        font-size: 1.25rem;
      }
    }

    hr {
      border-top: 2px solid $blue;
    }

    .remove-member {
      display: flex;
      padding: 0;
      font-size: 1rem;
      line-height: 2rem;
      z-index: 1;

      &,
      &:hover {
        text-decoration: none;
      }

      span {
        font-size: 2rem;
        line-height: 2rem;
        margin-right: 0.5rem;
      }
    }
  }
}
</style>
