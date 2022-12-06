<template>
    <v-snackbar :color="color" :timeout="timer" v-model="showSnackbar" bottom right>
        <v-icon left>{{ icon }}</v-icon>{{ message }}
    </v-snackbar>
</template>
  
<script>
    const DEFAULT_COLOR = "error";
    const DEFAULT_ICON = "mdi-alert";
    const DEFAULT_TIMER = 5000;
    export default {
        name: "SnackbarHelper",
        data() {
            return {
                showSnackbar: false,
                message: "",
                color: DEFAULT_COLOR,
                icon: DEFAULT_ICON,
                timer: DEFAULT_TIMER
            };
        },
        methods: {
            show(data) {
                this.message = data.message;
                this.color = Object.prototype.hasOwnProperty.call(data, "color") ? data.color : DEFAULT_COLOR;
                this.timer = Object.prototype.hasOwnProperty.call(data, "timer") ? data.timer : DEFAULT_TIMER;
                this.icon =  Object.prototype.hasOwnProperty.call(data, "icon") ? data.icon : DEFAULT_ICON;
                this.showSnackbar = true;
            }
        }
    }
</script>
