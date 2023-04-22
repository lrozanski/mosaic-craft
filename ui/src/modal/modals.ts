import {writable} from "svelte/store"

type ModalStore = {
    visible: boolean
}

function createConfirmModal() {
    const {subscribe, set} = writable<ModalStore>({
        visible: false,
    })

    return {
        subscribe,
        show: () => set({visible: true}),
        hide: () => set({visible: false}),
    }
}

export const modals = {
    confirm: createConfirmModal(),
}
