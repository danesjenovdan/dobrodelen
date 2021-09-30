<template>
  <div class="content">
    <content-title icon="signup-form" title="Пријава" />
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
              Драго ни е што одлучивте да ја регистрирате вашата организација на
              Навигаторот за граѓански органиации и да и покажете на пошироката
              јавност колку сте транспарентни и одговорни во вашата работа.
            </p>
            <p class="lead">
              Пред да започнете со внесување податоци за вашата организација,
              детално прочитајте ја методологијата. Оваа методологија е збир на
              критериуми со објаснувања и упатства за подготовка на податоците,
              во кои се претставени критериумите и условите за доделување поени,
              а посебно внимание се посветува на презентирање финансиски
              податоци, кои се бараат од вас да ги пополните.
            </p>
          </template>
          <template v-if="activeStage === 0">
            <form-category title="Име">
              <text-input
                v-model="data[activeStage].name"
                name="name"
                label="Официјално име на организацијата (од Централен регистар на Северна Македонија)"
                :has-error="dataErrors.name"
              />
              <text-input
                v-model="data[activeStage].additional_names"
                name="additional_names"
                label="Други имиња под кои е позната организацијата (кратенки, акроними)"
                :has-error="dataErrors.additional_names"
              />
            </form-category>

            <form-category title="Контакт">
              <text-input
                v-model="data[activeStage].contact_name"
                name="contact_name"
                label="Име и презиме"
                :has-error="dataErrors.contact_name"
              />
              <text-input
                v-model="data[activeStage].contact_email"
                name="contact_email"
                label="Е-мејл"
                :has-error="dataErrors.contact_email"
              />
              <text-input
                v-model="data[activeStage].contact_phone"
                name="contact_phone"
                label="Телефон"
                :has-error="dataErrors.contact_phone"
              />
            </form-category>

            <form-category title="Интернет (веб-страница, социјални мрежи)">
              <text-input
                v-model="data[activeStage].web_page"
                name="web_page"
                label="URL на веб -страница"
                :has-error="dataErrors.web_page"
              />
              <template v-for="(link, i) in data[activeStage].links">
                <text-input
                  :key="`link-${i}`"
                  v-model="link.url"
                  :name="`links__${i}`"
                  label="URL на профилот на социјалните медиуми"
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
                text="Додадете социјален профил"
                @click.native="data[activeStage].links.push({ url: null })"
              />
            </form-category>

            <form-category title="Слика">
              <file-input
                v-model="data[activeStage].cover_photo"
                name="cover_photo"
                label="Поставете слика"
                :has-error="dataErrors.cover_photo"
              />
            </form-category>

            <form-category title="Даночен број">
              <text-input
                v-model="data[activeStage].tax_number"
                name="tax_number"
                label="Даночен број"
                :has-error="dataErrors.tax_number"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 1">
            <form-category title="Мисија" note="максимум 500 карактери">
              <text-input
                v-model="data[activeStage].mission"
                name="mission"
                :multiline="9"
                :maxlength="500"
                :has-error="dataErrors.mission"
              />
            </form-category>

            <form-category title="Краток опис" note="максимум 1500 карактери">
              <text-input
                v-model="data[activeStage].description"
                name="description"
                :multiline="27"
                :maxlength="1500"
                :has-error="dataErrors.description"
              />
            </form-category>

            <form-category
              title="Области на делување"
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
                label="Друго:"
                custom-input
                :custom-input-value="data[activeStage].custom_area"
                @custom-change="data[activeStage].custom_area = $event"
              />
            </form-category>

            <form-category title="Сметка">
              <text-input
                v-model="data[activeStage].avg_revenue"
                name="avg_revenue"
                label="Просечен годишен буџет за последните три години"
                :has-error="dataErrors.avg_revenue"
              />
              <text-input
                v-model="data[activeStage].employed"
                name="employed"
                label="Број на вработени во последната завршена година"
                :has-error="dataErrors.employed"
              />
            </form-category>

            <form-category title="Статус">
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

            <form-category title="Региони" note="lahko izberete več možnosti">
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="[1, 2, 3, 4, 5, 6, 7, 8]"
                label="Сите"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="1"
                label="Вардарски"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="2"
                label="Источен"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="3"
                label="Југозападен"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="4"
                label="Југоисточен"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="5"
                label="Пелагониски"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="6"
                label="Полошки"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="7"
                label="Североисточен"
              />
              <selection-option
                v-model="data[activeStage].region"
                type="checkbox"
                name="region"
                :value="8"
                label="Скопски"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 2">
            <form-category title="Надзорен одбор">
              <selection-option
                v-model="data[activeStage].has_supervisory_board"
                type="checkbox"
                name="has_supervisory_board"
                label="Организацијата има надзорен одбор, кој се состана минатата година"
              />
              <text-input
                v-if="data[activeStage].has_supervisory_board"
                v-model="data[activeStage].supervisory_board_dates"
                name="supervisory_board_dates"
                label="Датуми на состаноци во претходната година"
                :has-error="dataErrors.supervisory_board_dates"
              />
            </form-category>
            <form-category
              v-if="data[activeStage].has_supervisory_board"
              title="Членови на Надзорниот одбор"
            >
              <template
                v-for="(member, i) in data[activeStage]
                  .supervisory_board_members"
              >
                <div :key="`supervisory_board_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`supervisory_board_members__name__${i}`"
                    label="Име и презиме"
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
                      label="Член"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="2"
                      label="Претставник на корисниците"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="3"
                      label="Претставник на вработените"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="4"
                      label="Претставник на основачите"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="5"
                      label="Именуван врз основа на роднински/пријателски врски"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="6"
                      label="Независен претставник"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`supervisory_board_members__role__${i}`"
                      value="7"
                      label="Друго:"
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
                    label="Тој добива награда за неговата работа во одборот"
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
                text="Додадете член"
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

            <form-category title="Управен одбор">
              <selection-option
                v-model="data[activeStage].has_management_board"
                type="checkbox"
                name="has_management_board"
                label="Организацијата има управен одбор, кој се состана минатата година"
              />
              <text-input
                v-if="data[activeStage].has_management_board"
                v-model="data[activeStage].management_board_dates"
                name="management_board_dates"
                label="Датуми на состаноци во претходната година"
                :has-error="dataErrors.management_board_dates"
              />
            </form-category>
            <form-category
              v-if="data[activeStage].has_management_board"
              title="Членови на управниот одбор"
            >
              <template
                v-for="(member, i) in data[activeStage]
                  .management_board_members"
              >
                <div :key="`management_board_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`management_board_members__name__${i}`"
                    label="Име и презиме"
                    :has-error="
                      dataErrors.management_board_members &&
                      dataErrors.management_board_members[i]
                    "
                  />
                  <div>
                    <h4>Povezava z organizacijo</h4>
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="1"
                      label="Член"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="2"
                      label="Претставник на корисниците"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="3"
                      label="Претставник на вработените"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="4"
                      label="Претставник на основачите"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="5"
                      label="Именуван врз основа на роднински/пријателски врски"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="6"
                      label="Независен претставник"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`management_board_members__role__${i}`"
                      value="7"
                      label="Друго:"
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
                    label="Тој добива награда за неговата работа во управниот одбор"
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
                text="Додадете член"
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

            <form-category title="Совет">
              <selection-option
                v-model="data[activeStage].has_council"
                type="checkbox"
                name="has_council"
                label="Организацијата има совет што се состана минатата година"
              />
              <text-input
                v-if="data[activeStage].has_council"
                v-model="data[activeStage].council_dates"
                name="council_dates"
                label="Датуми на состаноци во претходната година"
                :has-error="dataErrors.council_dates"
              />
            </form-category>
            <form-category
              v-if="data[activeStage].has_council"
              title="Членови на советот"
            >
              <template
                v-for="(member, i) in data[activeStage].council_members"
              >
                <div :key="`council_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`council_members__name__${i}`"
                    label="Име и презиме"
                    :has-error="
                      dataErrors.council_members &&
                      dataErrors.council_members[i]
                    "
                  />
                  <div>
                    <h4>Povezava z organizacijo</h4>
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="1"
                      label="Член"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="2"
                      label="Претставник на корисниците"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="3"
                      label="Претставник на вработените"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="4"
                      label="Претставник на основачите"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="5"
                      label="Именуван врз основа на роднински/пријателски врски"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="6"
                      label="Независен претставник"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`council_members__role__${i}`"
                      value="7"
                      label="Друго:"
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
                    label="Тој добива награда за неговата работа во советот"
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
                text="Додадете член"
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

            <form-category title="Друго">
              <selection-option
                v-model="data[activeStage].has_other_board"
                type="checkbox"
                name="has_other_board"
                label="Организацијата има друг орган кој ја извршува функцијата на надзор врз извршната канцеларија и се состана минатата година"
              />
              <text-input
                v-if="data[activeStage].has_other_board"
                v-model="data[activeStage].other_board_name"
                name="other_board_name"
                label="Име на органот"
                :has-error="dataErrors.other_board_dates"
              />
              <text-input
                v-if="data[activeStage].has_other_board"
                v-model="data[activeStage].other_board_dates"
                name="other_board_dates"
                label="Датуми на состаноци во претходната година"
                :has-error="dataErrors.other_board_dates"
              />
            </form-category>
            <form-category
              v-if="data[activeStage].has_other_board"
              title="Членови на телото"
            >
              <template
                v-for="(member, i) in data[activeStage].other_board_members"
              >
                <div :key="`other_board_members__${i}`">
                  <text-input
                    v-model="member.name"
                    :name="`other_board_members__name__${i}`"
                    label="Име и презиме"
                    :has-error="
                      dataErrors.other_board_members &&
                      dataErrors.other_board_members[i]
                    "
                  />
                  <div>
                    <h4>Povezava z organizacijo</h4>
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="1"
                      label="Член"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="2"
                      label="Претставник на корисниците"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="3"
                      label="Претставник на вработените"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="4"
                      label="Претставник на основачите"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="5"
                      label="Именуван врз основа на роднински/пријателски врски"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="6"
                      label="Независен претставник"
                    />
                    <selection-option
                      v-model="member.role"
                      type="radio"
                      :name="`other_board_members__role__${i}`"
                      value="7"
                      label="Друго:"
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
                    label="Тој добива награда за неговата работа во органот"
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
                text="Додадете член"
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

            <form-category title="Записник од состанокот">
              <selection-option
                v-model="data[activeStage].has_minutes_meeting"
                type="checkbox"
                name="has_minutes_meeting"
                label="Организацијата води записници од состаноците на не-извршните органи"
              />
              <file-input
                v-if="data[activeStage].has_minutes_meeting"
                v-model="data[activeStage].minutes_meeting"
                name="minutes_meeting"
                label="Прикачете го записникот од последниот состанок"
              />
            </form-category>

            <form-category title="Стратешко планирање">
              <selection-option
                v-model="data[activeStage].strategic_planning"
                type="checkbox"
                name="strategic_planning"
                label="Организацијата спроведува стратешко планирање"
              />
              <div v-if="data[activeStage].strategic_planning">
                <selection-option
                  v-model="data[activeStage].has_milestiones_description"
                  type="checkbox"
                  name="has_milestiones_description"
                  label="Организацијата го следи постигнувањето на стратешкиот план / цели"
                />
                <text-input
                  v-if="data[activeStage].has_milestiones_description"
                  v-model="data[activeStage].milestiones_description"
                  name="milestiones_description"
                  label="Краток опис за тоа (максимум 500 карактери)"
                  :multiline="9"
                  :maxlength="500"
                  :has-error="dataErrors.milestiones_description"
                />

                <selection-option
                  v-model="data[activeStage].has_strategic_goals"
                  type="checkbox"
                  name="has_strategic_goals"
                  label="Организацијата подготвува извештаи за следење на стратешкиот план / цели"
                />
                <file-input
                  v-if="data[activeStage].has_strategic_goals"
                  v-model="data[activeStage].strategic_goals"
                  name="strategic_goals"
                  label="Прикачи извештај"
                  :has-error="dataErrors.strategic_goals"
                />
              </div>
            </form-category>
          </template>

          <template v-else-if="activeStage === 3">
            <form-category title="Финансиски извештај">
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
                label="Прикачете финансиски извештај"
              />
            </form-category>

            <form-category
              title="Финансиски извештај (завршна сметка) доставен до Централен регистар на Северна Македонија"
            >
              <file-input
                v-model="data[activeStage].finance_report_ajpes"
                name="finance_report_ajpes"
                label="Прикачете го тој извештај"
              />
            </form-category>

            <form-category title="Revidiranje finančnega poročila">
              <selection-option
                v-model="data[activeStage].has_audited_report"
                type="checkbox"
                name="has_audited_report"
                label="Organizacija ima revidirana finančna poročila"
              />
              <file-input
                v-if="data[activeStage].has_audited_report"
                v-model="data[activeStage].audited_report"
                name="audited_report"
                label="Priložite revidirano poročilo"
              />
            </form-category>

            <form-category title="Финансиски план">
              <selection-option
                v-model="data[activeStage].has_finance_plan"
                type="checkbox"
                name="has_finance_plan"
                label="Организацијата има финансиски план за тековната година"
              />
              <file-input
                v-if="data[activeStage].has_finance_plan"
                v-model="data[activeStage].finance_plan"
                name="finance_plan"
                label="Прикачете финансиски план"
              />
            </form-category>

            <!-- <form-category title="Posojila">
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
            </form-category> -->

            <form-category title="Плата">
              <selection-option
                v-model="data[activeStage].has_payment_classes"
                type="checkbox"
                name="has_payment_classes"
                label="Организацијата има листа на работни места и плати"
              />
              <file-input
                v-if="data[activeStage].has_payment_classes"
                v-model="data[activeStage].payment_classes"
                name="payment_classes"
                label="Прикачете го документот"
              />

              <text-input
                v-model="data[activeStage].wages_ratio"
                name="wages_ratio"
                label="Односот помеѓу највисоката и просечната плата во организацијата"
                :has-error="dataErrors.wages_ratio"
              />
            </form-category>
          </template>

          <template v-else-if="activeStage === 4">
            <selection-option
              v-model="data[activeStage].has_published_work_reports"
              type="checkbox"
              name="has_published_work_reports"
              label="Организацијата објавува годишни организациски извештаи за работата"
            />
            <text-input
              v-if="data[activeStage].has_published_work_reports"
              v-model="data[activeStage].published_work_reports_url"
              name="published_work_reports_url"
              label="URL до објавените годишни извештаи за работата"
              :has-error="dataErrors.published_work_reports_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_financial_reports"
              type="checkbox"
              name="has_published_financial_reports"
              label="Организацијата објавува годишни финансиски извештаи"
            />
            <text-input
              v-if="data[activeStage].has_published_financial_reports"
              v-model="data[activeStage].published_financial_reports_url"
              name="published_financial_reports_url"
              label="URL до објавените финансиски извештаи"
              :has-error="dataErrors.published_financial_reports_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_executive_salaries"
              type="checkbox"
              name="has_published_executive_salaries"
              label="Објавен е надоместокот на раководството"
            />
            <text-input
              v-if="data[activeStage].has_published_executive_salaries"
              v-model="data[activeStage].published_executive_salaries_url"
              name="published_executive_salaries_url"
              label="URL до објавениот надоместок за раковдоството"
              :has-error="dataErrors.published_executive_salaries_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_salary_ratio"
              type="checkbox"
              name="has_published_salary_ratio"
              label="Објавен е односот помеѓу платите"
            />
            <text-input
              v-if="data[activeStage].has_published_salary_ratio"
              v-model="data[activeStage].published_salary_ratio_url"
              name="published_salary_ratio_url"
              label="URL до објавата за однос на платите"
              :has-error="dataErrors.published_salary_ratio_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_employee_list"
              type="checkbox"
              name="has_published_employee_list"
              label="Објавена е листа на клучни вработени"
            />
            <text-input
              v-if="data[activeStage].has_published_employee_list"
              v-model="data[activeStage].published_employee_list_url"
              name="published_employee_list_url"
              label="URL до објавената листа на клучни вработени"
              :has-error="dataErrors.published_employee_list_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_board_members"
              type="checkbox"
              name="has_published_board_members"
              label="Објавени се членовите на Управниот одбор / Надзорниот одбор"
            />
            <text-input
              v-if="data[activeStage].has_published_board_members"
              v-model="data[activeStage].published_board_members_url"
              name="published_board_members_url"
              label="URL до објавената листа на членови на Управниот / Надзорниот одбор"
              :has-error="dataErrors.published_board_members_url"
            />
            <selection-option
              v-model="data[activeStage].has_published_financial_plan"
              type="checkbox"
              name="has_published_financial_plan"
              label="Објавен е финансискиот план за тековната година"
            />
            <text-input
              v-if="data[activeStage].has_published_financial_plan"
              v-model="data[activeStage].published_financial_plan_url"
              name="published_financial_plan_url"
              label="URL до објавениот финансиски план за тековната година"
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
  async asyncData({ $axios, query, error }) {
    const editId = query.edit_id || null;
    const editKey = query.edit_key || null;

    let initialData = {};
    if (editId && editKey) {
      initialData = await $axios.$get(
        `/api/organizations/${editId}/?edit_key=${editKey}`,
      );
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
        region: initialData.region ? initialData.region.slice() : [],
        avg_revenue: initialData.avg_revenue || 0,
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
          initialData.supervisory_board_members &&
          initialData.supervisory_board_members.length
            ? cloneDeep(initialData.supervisory_board_members)
            : [{ name: '', role: '1', custom_role: '', is_paid: false }],
        has_management_board: initialData.has_management_board || false,
        management_board_dates: initialData.management_board_dates || '',
        management_board_members:
          initialData.management_board_members &&
          initialData.management_board_members.length
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
          initialData.other_board_members &&
          initialData.other_board_members.length
            ? cloneDeep(initialData.other_board_members)
            : [{ name: '', role: '1', custom_role: '', is_paid: false }],
        //
        has_minutes_meeting: initialData.has_minutes_meeting || false,
        minutes_meeting: initialData.minutes_meeting || null,
        strategic_planning: initialData.strategic_planning || false,
        has_milestiones_description:
          initialData.has_milestiones_description || false,
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
        has_published_work_reports:
          initialData.has_published_work_reports || false,
        published_work_reports_url:
          initialData.published_work_reports_url || null,
        has_published_financial_reports:
          initialData.has_published_financial_reports || false,
        published_financial_reports_url:
          initialData.published_financial_reports_url || null,
        has_published_executive_salaries:
          initialData.has_published_executive_salaries || false,
        published_executive_salaries_url:
          initialData.published_executive_salaries_url || null,
        has_published_salary_ratio:
          initialData.has_published_salary_ratio || false,
        published_salary_ratio_url:
          initialData.published_salary_ratio_url || null,
        has_published_employee_list:
          initialData.has_published_employee_list || false,
        published_employee_list_url:
          initialData.published_employee_list_url || null,
        has_published_board_members:
          initialData.has_published_board_members || false,
        published_board_members_url:
          initialData.published_board_members_url || null,
        has_published_financial_plan:
          initialData.has_published_financial_plan || false,
        published_financial_plan_url:
          initialData.published_financial_plan_url || null,
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
  head() {
    return {
      title: 'Пријава',
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
      const method = this.editId && this.editKey ? 'patch' : 'post';
      const query = `${this.editKey ? `?edit_key=${this.editKey}` : ''}`;
      const url = `/api/organizations/${
        this.editId ? `${this.editId}/` : ''
      }${query}`;
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
