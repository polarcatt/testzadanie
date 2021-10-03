 <template>
 <transition name="fade" appear>
            <div class="modal-overlay">
                <div class="modal">
                    <div>
                        Вы уверены, что хотите удалить элемент?
                    </div>
                    <div>
                        <button class="button toright comp-margin" @click="Close()">
                        Закрыть
                        </button>
                        <button class="button toright comp-margin" @click="Confirm()">
                        Подтвердить
                        </button>
                    </div>
                </div>
            </div>
        </transition>
</template>

<script>
export default {
    name: 'modal',

    props: {
        indexq: Number,
    },

    data() {
        return{
            index: this.indexq,
        }
    },

    methods:{

        Close:function () {
            this.$emit('close')
        },

        Confirm:function () {
            this.$emit('confirm', this.index)
        },
    }
}
</script>

<style>
    .app {
        font-family: serif;
        font-size: 17px;
        margin-top: 10px;
        margin-left: 20px;
        margin-right: 20px;
    }

    div.modal tr{
        text-align: right;
    }

    .comp-margin {
        margin: 5px;
    }

    div.message {
        background-color: #EEBBBB;
        width: 100%;
    }

    div.change{
        border-color:#AAAAAA;
        border-style: solid;
        border-width: 0px 0px 1px 0px;
        padding-bottom: 5px;
        margin-bottom: 10px;
    }
    .toright{
        float:right;
    }
    button:hover{
        background-color:#5599DD;
        color:#DDDDDD;
    }   
    .modal-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
    }
    .modal {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        max-width: 350px;
        background-color: #FFFFFF;
        padding: 25px;
        display: block;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .3s ease;
    }
    .fade-enter-from, .fade-leave-to {
        opacity: 0;
    }
</style>