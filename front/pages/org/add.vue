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
                id="exampleInputEmail1"
                type="email"
                class="form-control"
                aria-describedby="emailHelp"
                placeholder="Email address"
              />
              <label for="exampleInputEmail1">Email address</label>
              <!-- <small
                id="emailHelp"
                class="form-text text-muted"
              >We'll never share your email with anyone else.</small>-->
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
    }

    .form-group {
      display: flex;
      flex-direction: column-reverse;

      .form-control,
      label {
        transition: all 0.2s;
      }

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
      }

      label {
        font-weight: 400;
        font-size: 0.9375rem;
        line-height: 1;
        margin-bottom: -1em;
        margin-left: 2rem;
        transform: translate(0, 0.75rem) scale(1);
        cursor: text;
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
        transform: translate(0, 0.75rem) scale(1);
      }
    }
  }
}
</style>
