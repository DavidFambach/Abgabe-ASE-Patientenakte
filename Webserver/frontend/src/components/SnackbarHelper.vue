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
        name: "snackbar-helper",
        data() {
            return {
                showSnackbar: false,
                active: false,
                queue: [],
                message: "",
                color: DEFAULT_COLOR,
                icon: DEFAULT_ICON,
                timer: DEFAULT_TIMER
            };
        },
        methods: {
            show(data) {
                if(this.active)
                    this.queue.push(data);
                else
                    this._showNow(data);
            },
            _showNow(data) {
                const delay = Object.prototype.hasOwnProperty.call(data, "timer") ? data.timer : DEFAULT_TIMER;
                const fade = 400;
                this.active = true;
                this.message = data.message;
                this.color = Object.prototype.hasOwnProperty.call(data, "color") ? data.color : DEFAULT_COLOR;
                this.timer = delay;
                this.icon = Object.prototype.hasOwnProperty.call(data, "icon") ? data.icon : DEFAULT_ICON;
                this.showSnackbar = true;
                setTimeout((() => {
                    if(this.queue.length > 0) {
                        const next = this.queue.splice(0, 1)[0];
                        this._showNow(next);
                    } else {
                        this.active = false;
                    }
                }).bind(this), delay + fade);
            }
        }
    }
</script>
