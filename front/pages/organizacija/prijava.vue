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
          <template v-if="activeStage === -1">
            <p class="lead">
              Veseli nas, da ste se odločili vpisati vašo organizacijo na spletno stran
              <em>dobrodelen.si</em> in širši javnosti pokazati, kako transparenti in odgovorni ste
              pri svojem poslovanju.
            </p>
            <p class="lead">
              <!-- eslint-disable prettier/prettier -->
              Preden začnete z vpisovanjem podatkov o vaši organizaciji podrobno preberite
              <a
                :href="`${apiBaseUrl}/documents/2/Smernice_dobrodelen.si_FINAL.pdf`"
                target="_blank"
                rel="noopener noreferrer"
              >Metodologijo za ocenjevanje in razvrščanje slovenskih nevladnih organizacij – Nabor
                kriterijev s pojasnili in smernice za pripravo podatkov</a>,
              kjer so predstavljeni kriteriji in pogoji za dodelitev točk, posebna pozornost pa
              je namenjena predstavitvi finančnih podatkov, ki jih bomo od vas potrebovali in kako
              morajo biti pripravljeni.
              <!-- eslint-enable prettier/prettier -->
            </p>
          </template>
          <template v-if="activeStage === 0">
            <form-category title="Ime">
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

            <form-category title="Spletna prisotnost">
              <text-input
                v-model="data[activeStage].web_page"
                name="web_page"
                label="URL spletne strani"
                :has-error="dataErrors.web_page"
              />
              <template v-for="(link, i) in data[activeStage].links">
                <text-input
                  :key="`link-${i}`"
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

            <form-category title="Slika">
              <file-input
                v-model="data[activeStage].cover_photo"
                name="cover_photo"
                label="Naložite sliko"
                :has-error="dataErrors.cover_photo"
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
          </template>

          <template v-else-if="activeStage === 1">
            <form-category title="Poslanstvo" note="največ 500 znakov">
              <text-input
                v-model="data[activeStage].mission"
                name="mission"
                :multiline="9"
                :maxlength="500"
                :has-error="dataErrors.mission"
              />
            </form-category>

            <form-category title="Kratek opis" note="največ 1500 znakov">
              <text-input
                v-model="data[activeStage].description"
                name="description"
                :multiline="27"
                :maxlength="1500"
                :has-error="dataErrors.description"
              />
            </form-category>

            <form-category title="Področja delovanja" note="lahko izberete več možnosti">
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
                :value="10"
                label="Drugo:"
                custom-input
                :custom-input-value="data[activeStage].custom_area"
                @custom-change="data[activeStage].custom_area = $event"
              />
            </form-category>

            <form-category title="Proračun">
              <text-input
                v-model="data[activeStage].avg_revenue"
                name="avg_revenue"
                label="Povprečni letni proračun v zadnjih treh letih"
                :has-error="dataErrors.avg_revenue"
              />
              <text-input
                v-model="data[activeStage].employed"
                name="employed"
                label="Število zaposlenih v zadnjem zaključenem letu"
                :has-error="dataErrors.employed"
              />
            </form-category>

            <form-category title="Statusi">
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
                label="Organizacija je na seznamu upravičencev do 0,5 % dohodnine"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 2">
            <form-category title="Nadzorni odbor">
              <selection-option
                v-model="data[activeStage].has_supervisory_board"
                type="checkbox"
                name="has_supervisory_board"
                label="Organizacija ima nadzorni odbor, ki se je v preteklem letu srečal"
              />
              <text-input
                v-if="data[activeStage].has_supervisory_board"
                v-model="data[activeStage].supervisory_board_dates"
                name="supervisory_board_dates"
                label="Datumi srečanj v preteklem letu"
                :has-error="dataErrors.supervisory_board_dates"
              />
            </form-category>
            <form-category
              v-if="data[activeStage].has_supervisory_board"
              title="Člani nadzornega odbora"
            >
              <template v-for="(member, i) in data[activeStage].supervisory_board_members">
                <div :key="`supervisory_board_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`supervisory_board_members__name__${i}`"
                    label="Ime in priimek"
                    :has-error="
                      dataErrors.supervisory_board_members &&
                        dataErrors.supervisory_board_members[i]
                    "
                  />
                  <div>
                    <h4>Povezava z organizacijo</h4>
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="1"
                      label="Član"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="2"
                      label="Predstavnik uporabnikov"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="3"
                      label="Predstavnik zaposlenih"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="4"
                      label="Predstavnik ustanoviteljev"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="5"
                      label="Imenovan na podlagi sorodstvenih/prijateljskih vezi"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="6"
                      label="Neodvisni predstavnik"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="7"
                      label="Drugo:"
                      custom-input
                      :custom-input-value="member.custom_role"
                      @custom-change="member.custom_role = $event"
                    />
                  </div>
                  <h4>Nadomestilo</h4>
                  <selection-option
                    v-model="member.is_paid"
                    type="checkbox"
                    :name="`supervisory_board_members__is_paid__${i}`"
                    label="Za svoje delo v odboru prejema nadomestilo"
                  />
                  <hr />
                  <br />
                </div>
              </template>
              <button
                v-if="data[activeStage].supervisory_board_members.length"
                type="button"
                class="btn btn-link remove-member"
                @click="data[activeStage].supervisory_board_members.pop()"
              >
                <span>&times;</span> Odstrani člana
              </button>
              <add-button
                text="Dodajte člana"
                @click.native="
                  data[activeStage].supervisory_board_members.push({
                    name: '',
                    role: '1',
                    custom_role: '',
                    is_paid: false,
                  })
                "
              />
            </form-category>

            <form-category title="Upravni odbor">
              <selection-option
                v-model="data[activeStage].has_management_board"
                type="checkbox"
                name="has_management_board"
                label="Organizacija ima upravni odbor, ki se je v preteklem letu srečal"
              />
              <text-input
                v-if="data[activeStage].has_management_board"
                v-model="data[activeStage].management_board_dates"
                name="management_board_dates"
                label="Datumi srečanj v preteklem letu"
                :has-error="dataErrors.management_board_dates"
              />
            </form-category>
            <form-category
              v-if="data[activeStage].has_management_board"
              title="Člani upravnega odbora"
            >
              <template v-for="(member, i) in data[activeStage].management_board_members">
                <div :key="`management_board_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`management_board_members__name__${i}`"
                    label="Ime in priimek"
                    :has-error="
                      dataErrors.management_board_members && dataErrors.management_board_members[i]
                    "
                  />
                  <div>
                    <h4>Povezava z organizacijo</h4>
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="1"
                      label="Član"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="2"
                      label="Predstavnik uporabnikov"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="3"
                      label="Predstavnik zaposlenih"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="4"
                      label="Predstavnik ustanoviteljev"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="5"
                      label="Imenovan na podlagi sorodstvenih/prijateljskih vezi"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="6"
                      label="Neodvisni predstavnik"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="7"
                      label="Drugo:"
                      custom-input
                      :custom-input-value="member.custom_role"
                      @custom-change="member.custom_role = $event"
                    />
                  </div>
                  <h4>Nadomestilo</h4>
                  <selection-option
                    v-model="member.is_paid"
                    type="checkbox"
                    :name="`management_board_members__is_paid__${i}`"
                    label="Za svoje delo v odboru prejema nadomestilo"
                  />
                  <hr />
                  <br />
                </div>
              </template>
              <button
                v-if="data[activeStage].management_board_members.length"
                type="button"
                class="btn btn-link remove-member"
                @click="data[activeStage].management_board_members.pop()"
              >
                <span>&times;</span> Odstrani člana
              </button>
              <add-button
                text="Dodajte člana"
                @click.native="
                  data[activeStage].management_board_members.push({
                    name: '',
                    role: '1',
                    custom_role: '',
                    is_paid: false,
                  })
                "
              />
            </form-category>

            <form-category title="Svet zavoda">
              <selection-option
                v-model="data[activeStage].has_council"
                type="checkbox"
                name="has_council"
                label="Organizacija ima svet zavoda, ki se je v preteklem letu srečal"
              />
              <text-input
                v-if="data[activeStage].has_council"
                v-model="data[activeStage].council_dates"
                name="council_dates"
                label="Datumi srečanj v preteklem letu"
                :has-error="dataErrors.council_dates"
              />
            </form-category>
            <form-category v-if="data[activeStage].has_council" title="Člani sveta zavoda">
              <template v-for="(member, i) in data[activeStage].council_members">
                <div :key="`council_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`council_members__name__${i}`"
                    label="Ime in priimek"
                    :has-error="dataErrors.council_members && dataErrors.council_members[i]"
                  />
                  <div>
                    <h4>Povezava z organizacijo</h4>
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="1"
                      label="Član"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="2"
                      label="Predstavnik uporabnikov"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="3"
                      label="Predstavnik zaposlenih"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="4"
                      label="Predstavnik ustanoviteljev"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="5"
                      label="Imenovan na podlagi sorodstvenih/prijateljskih vezi"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="6"
                      label="Neodvisni predstavnik"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="7"
                      label="Drugo:"
                      custom-input
                      :custom-input-value="member.custom_role"
                      @custom-change="member.custom_role = $event"
                    />
                  </div>
                  <h4>Nadomestilo</h4>
                  <selection-option
                    v-model="member.is_paid"
                    type="checkbox"
                    :name="`council_members__is_paid__${i}`"
                    label="Za svoje delo v odboru prejema nadomestilo"
                  />
                  <hr />
                  <br />
                </div>
              </template>
              <button
                v-if="data[activeStage].council_members.length"
                type="button"
                class="btn btn-link remove-member"
                @click="data[activeStage].council_members.pop()"
              >
                <span>&times;</span> Odstrani člana
              </button>
              <add-button
                text="Dodajte člana"
                @click.native="
                  data[activeStage].council_members.push({
                    name: '',
                    role: '1',
                    custom_role: '',
                    is_paid: false,
                  })
                "
              />
            </form-category>

            <form-category title="Drugo">
              <selection-option
                v-model="data[activeStage].has_other_board"
                type="checkbox"
                name="has_other_board"
                label="Organizacija ima drug organ, ki se je v preteklem letu srečal"
              />
              <text-input
                v-if="data[activeStage].has_other_board"
                v-model="data[activeStage].other_board_name"
                name="other_board_name"
                label="Ime organa"
                :has-error="dataErrors.other_board_dates"
              />
              <text-input
                v-if="data[activeStage].has_other_board"
                v-model="data[activeStage].other_board_dates"
                name="other_board_dates"
                label="Datumi srečanj v preteklem letu"
                :has-error="dataErrors.other_board_dates"
              />
            </form-category>
            <form-category v-if="data[activeStage].has_other_board" title="Člani organa">
              <template v-for="(member, i) in data[activeStage].other_board_members">
                <div :key="`other_board_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`other_board_members__name__${i}`"
                    label="Ime in priimek"
                    :has-error="dataErrors.other_board_members && dataErrors.other_board_members[i]"
                  />
                  <div>
                    <h4>Povezava z organizacijo</h4>
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="1"
                      label="Član"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="2"
                      label="Predstavnik uporabnikov"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="3"
                      label="Predstavnik zaposlenih"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="4"
                      label="Predstavnik ustanoviteljev"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="5"
                      label="Imenovan na podlagi sorodstvenih/prijateljskih vezi"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="6"
                      label="Neodvisni predstavnik"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="7"
                      label="Drugo:"
                      custom-input
                      :custom-input-value="member.custom_role"
                      @custom-change="member.custom_role = $event"
                    />
                  </div>
                  <h4>Nadomestilo</h4>
                  <selection-option
                    v-model="member.is_paid"
                    type="checkbox"
                    :name="`other_board_members__is_paid__${i}`"
                    label="Za svoje delo v odboru prejema nadomestilo"
                  />
                  <hr />
                  <br />
                </div>
              </template>
              <button
                v-if="data[activeStage].other_board_members.length"
                type="button"
                class="btn btn-link remove-member"
                @click="data[activeStage].other_board_members.pop()"
              >
                <span>&times;</span> Odstrani člana
              </button>
              <add-button
                text="Dodajte člana"
                @click.native="
                  data[activeStage].other_board_members.push({
                    name: '',
                    role: '1',
                    custom_role: '',
                    is_paid: false,
                  })
                "
              />
            </form-category>

            <form-category title="Zapisniki seje">
              <selection-option
                v-model="data[activeStage].has_minutes_meeting"
                type="checkbox"
                name="has_minutes_meeting"
                label="Organizacija vodi zapisnike sej"
              />
              <file-input
                v-if="data[activeStage].has_minutes_meeting"
                v-model="data[activeStage].minutes_meeting"
                name="minutes_meeting"
                label="Priložite zapisnik zadnje seje"
              />
            </form-category>

            <form-category title="Strateško načrtovanje">
              <selection-option
                v-model="data[activeStage].strategic_planning"
                type="checkbox"
                name="strategic_planning"
                label="Organizacija strateško načrtuje"
              />
              <div v-if="data[activeStage].strategic_planning">
                <selection-option
                  v-model="data[activeStage].has_milestiones_description"
                  type="checkbox"
                  name="has_milestiones_description"
                  label="Organizacija spremlja doseganje strateških ciljev"
                />
                <text-input
                  v-if="data[activeStage].has_milestiones_description"
                  v-model="data[activeStage].milestiones_description"
                  name="milestiones_description"
                  label="Kratek opis kako (največ 500 znakov)"
                  :multiline="9"
                  :maxlength="500"
                  :has-error="dataErrors.milestiones_description"
                />

                <selection-option
                  v-model="data[activeStage].has_strategic_goals"
                  type="checkbox"
                  name="has_strategic_goals"
                  label="Organizacija vodi pisna poročila o spremljanju stateških ciljev"
                />
                <file-input
                  v-if="data[activeStage].has_strategic_goals"
                  v-model="data[activeStage].strategic_goals"
                  name="strategic_goals"
                  label="Priložite poročilo"
                  :has-error="dataErrors.strategic_goals"
                />
              </div>
            </form-category>
          </template>

          <template v-else-if="activeStage === 3">
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
                v-model="data[activeStage].finance_report"
                name="finance_report"
                label="Priložite finančno poročilo"
              />
            </form-category>

            <form-category title="Finančno poročilo, ki je bilo oddano na AJPES">
              <file-input
                v-model="data[activeStage].finance_report_ajpes"
                name="finance_report_ajpes"
                label="Priložite finančno poročilo"
              />
            </form-category>

            <form-category title="Revidiranje finančnega poročila">
              <selection-option
                v-model="data[activeStage].has_audited_report"
                type="checkbox"
                name="has_audited_report"
                label="Organizacija je dolžna revidirati svoja finančna poročila"
              />
              <file-input
                v-if="data[activeStage].has_audited_report"
                v-model="data[activeStage].audited_report"
                name="audited_report"
                label="Priložite revidirano poročilo"
              />
            </form-category>

            <form-category title="Finančni načrt">
              <selection-option
                v-model="data[activeStage].has_finance_plan"
                type="checkbox"
                name="has_finance_plan"
                label="Organizacija ima finančni načrt za tekoče leto"
              />
              <file-input
                v-if="data[activeStage].has_finance_plan"
                v-model="data[activeStage].finance_plan"
                name="finance_plan"
                label="Priložite finančni načrt"
              />
            </form-category>

            <form-category title="Posojila">
              <selection-option
                v-model="data[activeStage].has_given_loans"
                type="checkbox"
                name="has_given_loans"
                label="Organizacija daje posojila povezanim osebam (zaposleni, člani upravnega/nadzornega odbora in njihovi družinski člani, ...)"
              />
              <file-input
                v-if="data[activeStage].has_given_loans"
                v-model="data[activeStage].given_loan"
                name="given_loan"
                label="Priložite seznam danih posojil"
              />

              <selection-option
                v-model="data[activeStage].has_received_loans"
                type="checkbox"
                name="has_received_loans"
                label="Organizacija prejema posojila od povezanih oseb (zaposleni, člani upravnega/nadzornega odbora in njihovi družinski člani, ...)"
              />
              <file-input
                v-if="data[activeStage].has_received_loans"
                v-model="data[activeStage].received_loans"
                name="received_loans"
                label="Priložite seznam prejetih posojil"
              />
            </form-category>

            <form-category title="Plačilni razredi">
              <selection-option
                v-model="data[activeStage].has_payment_classes"
                type="checkbox"
                name="has_payment_classes"
                label="Organizacija ima akt o sistematizaciji delovnih mest in plačnih razredov"
              />
              <file-input
                v-if="data[activeStage].has_payment_classes"
                v-model="data[activeStage].payment_classes"
                name="payment_classes"
                label="Priložite akt"
              />

              <text-input
                v-model="data[activeStage].wages_ratio"
                name="wages_ratio"
                label="Razmerje med najvišjo in povprečno plačo v organizaciji"
                :has-error="dataErrors.wages_ratio"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 4">
            <selection-option
              v-model="data[activeStage].has_published_work_reports"
              type="checkbox"
              name="has_published_work_reports"
              label="Organizacija ima objavljena letna poročila o delu"
            />
            <text-input
              v-if="data[activeStage].has_published_work_reports"
              v-model="data[activeStage].published_work_reports_url"
              name="published_work_reports_url"
              label="URL do objavljenih letnih poročil o delu"
              :has-error="dataErrors.published_work_reports_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_financial_reports"
              type="checkbox"
              name="has_published_financial_reports"
              label="Organizacija ima objavljena letna finančna poročila"
            />
            <text-input
              v-if="data[activeStage].has_published_financial_reports"
              v-model="data[activeStage].published_financial_reports_url"
              name="published_financial_reports_url"
              label="URL do objavljenih finančnih poročil"
              :has-error="dataErrors.published_financial_reports_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_executive_salaries"
              type="checkbox"
              name="has_published_executive_salaries"
              label="Objavljene so plače vodstva"
            />
            <text-input
              v-if="data[activeStage].has_published_executive_salaries"
              v-model="data[activeStage].published_executive_salaries_url"
              name="published_executive_salaries_url"
              label="URL do objavljenih plač vodstva"
              :has-error="dataErrors.published_executive_salaries_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_salary_ratio"
              type="checkbox"
              name="has_published_salary_ratio"
              label="Objavljeno je razmerje med plačami"
            />
            <text-input
              v-if="data[activeStage].has_published_salary_ratio"
              v-model="data[activeStage].published_salary_ratio_url"
              name="published_salary_ratio_url"
              label="URL do objavljenih razmerij med plačami"
              :has-error="dataErrors.published_salary_ratio_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_employee_list"
              type="checkbox"
              name="has_published_employee_list"
              label="Objavljen je seznam ključnih zaposlenih"
            />
            <text-input
              v-if="data[activeStage].has_published_employee_list"
              v-model="data[activeStage].published_employee_list_url"
              name="published_employee_list_url"
              label="URL do objavljenega seznama ključnih zaposlenih"
              :has-error="dataErrors.published_employee_list_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_board_members"
              type="checkbox"
              name="has_published_board_members"
              label="Obljavljeni so člani nadzornega/upravnega odbora"
            />
            <text-input
              v-if="data[activeStage].has_published_board_members"
              v-model="data[activeStage].published_board_members_url"
              name="published_board_members_url"
              label="URL do objavljenega seznama članov odbora"
              :has-error="dataErrors.published_board_members_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_financial_plan"
              type="checkbox"
              name="has_published_financial_plan"
              label="Objavljen je finančni načrt za tekoče leto"
            />
            <text-input
              v-if="data[activeStage].has_published_financial_plan"
              v-model="data[activeStage].published_financial_plan_url"
              name="published_financial_plan_url"
              label="URL do objavljenega finančnega načrta za tekoče leto"
              :has-error="dataErrors.published_financial_plan_url"
            />
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
          label: 'Poslovanje',
        },
        {
          label: 'Finance',
        },
        {
          label: 'Transparentnost',
        },
      ],
      activeStage: -1,
      saving: false,
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
        custom_area: initialData.custom_area || '',
        avg_revenue: initialData.avg_revenue || '',
        employed: initialData.employed || 0,
        is_charity: initialData.is_charity || false,
        has_public_interest: initialData.has_public_interest || false,
        is_voluntary: initialData.is_voluntary || false,
        zero5: initialData.zero5 || false,
      },
      {
        //
        has_supervisory_board: initialData.has_supervisory_board || false,
        supervisory_board_dates: initialData.supervisory_board_dates || '',
        supervisory_board_members:
          initialData.supervisory_board_members && initialData.supervisory_board_members.length
            ? cloneDeep(initialData.supervisory_board_members)
            : [{ name: '', role: '1', custom_role: '', is_paid: false }],
        has_management_board: initialData.has_management_board || false,
        management_board_dates: initialData.management_board_dates || '',
        management_board_members:
          initialData.management_board_members && initialData.management_board_members.length
            ? cloneDeep(initialData.management_board_members)
            : [{ name: '', role: '1', custom_role: '', is_paid: false }],
        has_council: initialData.has_council || false,
        council_dates: initialData.council_dates || '',
        council_members:
          initialData.council_members && initialData.council_members.length
            ? cloneDeep(initialData.council_members)
            : [{ name: '', role: '1', custom_role: '', is_paid: false }],
        has_other_board: initialData.has_other_board || false,
        other_board_name: initialData.other_board_name || '',
        other_board_dates: initialData.other_board_dates || '',
        other_board_members:
          initialData.other_board_members && initialData.other_board_members.length
            ? cloneDeep(initialData.other_board_members)
            : [{ name: '', role: '1', custom_role: '', is_paid: false }],
        //
        has_minutes_meeting: initialData.has_minutes_meeting || false,
        minutes_meeting: initialData.minutes_meeting || null,
        strategic_planning: initialData.strategic_planning || false,
        has_milestiones_description: initialData.has_milestiones_description || false,
        milestiones_description: initialData.milestiones_description || '',
        has_strategic_goals: initialData.has_strategic_goals || false,
        strategic_goals: initialData.strategic_goals || null,
      },
      {
        finance_report: initialData.finance_report || null,
        finance_report_ajpes: initialData.finance_report_ajpes || null,
        has_audited_report: initialData.has_audited_report || false,
        audited_report: initialData.audited_report || null,
        has_finance_plan: initialData.has_finance_plan || false,
        finance_plan: initialData.finance_plan || null,
        has_given_loans: initialData.has_given_loans || false,
        given_loan: initialData.given_loan || null,
        has_received_loans: initialData.has_received_loans || false,
        received_loans: initialData.received_loans || null,
        has_payment_classes: initialData.has_payment_classes || false,
        payment_classes: initialData.payment_classes || null,
        wages_ratio: initialData.wages_ratio || '',
      },
      {
        has_published_work_reports: initialData.has_published_work_reports || false,
        published_work_reports_url: initialData.published_work_reports_url || null,
        has_published_financial_reports: initialData.has_published_financial_reports || false,
        published_financial_reports_url: initialData.published_financial_reports_url || null,
        has_published_executive_salaries: initialData.has_published_executive_salaries || false,
        published_executive_salaries_url: initialData.published_executive_salaries_url || null,
        has_published_salary_ratio: initialData.has_published_salary_ratio || false,
        published_salary_ratio_url: initialData.published_salary_ratio_url || null,
        has_published_employee_list: initialData.has_published_employee_list || false,
        published_employee_list_url: initialData.published_employee_list_url || null,
        has_published_board_members: initialData.has_published_board_members || false,
        published_board_members_url: initialData.published_board_members_url || null,
        has_published_financial_plan: initialData.has_published_financial_plan || false,
        published_financial_plan_url: initialData.published_financial_plan_url || null,
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
      if (data) {
        // Delete custom area if not selected
        if (data.area && data.area.filter((e) => e === 10).length === 0) {
          data.custom_area = '';
        }
        // Delete member placeholders if not selected
        if (data.has_supervisory_board === false) {
          data.supervisory_board_dates = '';
          data.supervisory_board_members = [];
        }
        if (data.has_management_board === false) {
          data.management_board_dates = '';
          data.management_board_members = [];
        }
        if (data.has_council === false) {
          data.council_dates = '';
          data.council_members = [];
        }
        if (data.has_other_board === false) {
          data.other_board_dates = '';
          data.other_board_members = [];
        }

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
          // Delete files if option not selected
          if (key === 'has_minutes_meeting') {
            if (data[key] === false) {
              data.minutes_meeting = null;
              jsonData.minutes_meeting = null;
            }
          }
          if (key === 'strategic_planning') {
            if (data[key] === false) {
              data.has_milestiones_description = false;
              jsonData.has_milestiones_description = false;
              data.milestiones_description = '';
              jsonData.milestiones_description = '';
              data.has_strategic_goals = false;
              jsonData.has_strategic_goals = false;
              data.strategic_goals = null;
              jsonData.strategic_goals = null;
            }
          }
          if (key === 'has_milestiones_description') {
            if (data[key] === false) {
              data.milestiones_description = '';
              jsonData.milestiones_description = '';
            }
          }
          if (key === 'has_strategic_goals') {
            if (data[key] === false) {
              data.strategic_goals = null;
              jsonData.strategic_goals = null;
            }
          }
          if (key === 'has_audited_report') {
            if (data[key] === false) {
              data.audited_report = null;
              jsonData.audited_report = null;
            }
          }
          if (key === 'has_finance_plan') {
            if (data[key] === false) {
              data.finance_plan = null;
              jsonData.finance_plan = null;
            }
          }
          if (key === 'has_given_loans') {
            if (data[key] === false) {
              data.given_loan = null;
              jsonData.given_loan = null;
            }
          }
          if (key === 'has_received_loans') {
            if (data[key] === false) {
              data.received_loans = null;
              jsonData.received_loans = null;
            }
          }
          if (key === 'has_payment_classes') {
            if (data[key] === false) {
              data.payment_classes = null;
              jsonData.payment_classes = null;
            }
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
                this.$set(this.dataErrors, key, error.response.data[key].join(', '));
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
    margin-top: 6rem;

    @include media-breakpoint-down(sm) {
      margin-top: 2rem;
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
