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
          <fieldset>
            <legend>Ime</legend>

            <div class="form-group">
              <input
                id="orgName"
                type="text"
                class="form-control"
                placeholder="Uradno ime organizacije"
              />
              <label for="orgName">Uradno ime organizacije</label>
            </div>
            <div class="form-group">
              <input id="orgNameOther" type="text" class="form-control" placeholder="Druga imena" />
              <label for="orgNameOther">Druga imena</label>
            </div>
          </fieldset>
          <fieldset>
            <legend>Kontakt</legend>

            <div class="form-group">
              <div class="invalid-feedback">* nepravilna telefonska številka</div>
              <input
                id="orgPhone"
                type="text"
                class="form-control is-invalid"
                placeholder="Telefon"
                value="+00 00 000 00 00"
              />
              <label for="orgPhone">Telefon</label>
            </div>
          </fieldset>
          <fieldset>
            <legend>Poslanstvo</legend>
            <small class="form-text">
              <span>* največ 500 znakov</span>
            </small>

            <div class="form-group">
              <textarea class="form-control" rows="8">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Soluta et sed voluptate voluptatum nihil, corrupti iusto tenetur quaerat doloremque eos ipsum facere dolore. Repellendus sed, hic impedit est libero veritatis.
              </textarea>
            </div>
          </fieldset>
          <fieldset>
            <legend>Področja delovanja</legend>
            <small class="form-text">
              <span>* lahko izberete več možnosti</span>
            </small>

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

export default {
  components: {
    ContentTitle,
    FormStages,
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

    legend {
      font-size: 1.85rem;
      font-weight: 300;
      letter-spacing: 0.2em;
      margin-bottom: 1.5rem;

      + small {
        margin-top: -1.5rem;
        margin-bottom: 1.5rem;
        font-size: 0.9375rem;
      }
    }

    .form-group {
      display: flex;
      flex-direction: column-reverse;
      overflow: hidden;
      margin-bottom: 3rem;

      .form-control {
        border: 0;
        background: rgba(#f6f2f0, 0.4);
        font-size: 1.85rem;
        font-weight: 300;
        padding: 1rem 2rem;
        padding: 1.5rem 2rem 0.25rem;
        height: 5rem;
        border-bottom: 2px solid rgba($blue, 0.3);

        &::placeholder {
          font-weight: 300;
          color: $body-color;
        }

        &,
        &:focus {
          outline: 0;
          box-shadow: none;
        }

        &:focus {
          border-bottom-color: $blue;
        }

        &.is-invalid {
          color: $red;
          border-bottom-color: rgba($red, 0.3);

          &:focus {
            border-bottom-color: $red;
          }
        }
      }

      textarea.form-control {
        height: auto;
        font-size: 1.5rem;
      }

      label {
        font-weight: 400;
        font-size: 0.9375rem;
        line-height: 1.1;
        margin-bottom: -1.1em;
        margin-left: 2rem;
        transform: translate(0.1rem, 0.75rem) scale(1);
        cursor: text;
        transition: all 0.2s;
      }

      .form-control::placeholder {
        opacity: 0;
      }

      .form-control:placeholder-shown + label {
        max-width: 80%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        cursor: text;
        font-weight: 300;
        transform-origin: left bottom;
        transform: translate(-0.075rem, 2.5rem) scale(1.97);
      }

      .form-control:not(:placeholder-shown) + label,
      .form-control:focus + label {
        font-weight: 400;
        transform: translate(0.1rem, 0.75rem) scale(1);
      }

      .invalid-feedback {
        display: block;
        font-size: 0.9375rem;
        padding: 0 2rem;
      }
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
  }
}
</style>
