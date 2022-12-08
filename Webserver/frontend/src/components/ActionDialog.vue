<template>

    <v-dialog v-model="visible">

        <v-card>
            <v-card-title>{{ title }}</v-card-title>
            <v-card-text>
                {{ text }}
                <br v-if="text != '' && $slots.extra != null" />
                <slot name="extra"></slot>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-spacer />
                <v-btn v-for="action in actions" :key="action.id" :color="action.color"
                    v-on:click="action.onclick()" text>
                    {{ action.text }}
                </v-btn>
            </v-card-actions>
        </v-card>

    </v-dialog>

</template>

<script>

    export default {
        name: "action-dialog",
        props: {
            prepare: Function
        },
        data: () => ({
            visible: false,
            title: "",
            text: "",
            actions: []
        }),
        methods: {
            open(title, text, actions) {
                if(this.prepare != null)
                    this.prepare();
                let id = 0;
                this.title = title;
                this.text = text;
                this.actions = actions.map(a => ({
                    id: id++,
                    text: a.text,
                    color: Object.prototype.hasOwnProperty.call(a, "color") ? a.color : "secondary",
                    onclick: (Object.prototype.hasOwnProperty.call(a, "onclick") ?
                        () => {
                            this.visible = false;
                            a.onclick();
                        } :
                        () => {
                            this.visible = false;
                        }
                    ).bind(this)
                }));
                this.visible = true;
            },
            close() {
                this.visible = false;
                this.title = "";
                this.text = "";
                this.actions = [];
            }
        }
    };

</script>
