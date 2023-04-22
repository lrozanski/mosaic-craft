<script lang="ts">
    import {get} from "svelte/store"
    import Modal from "./Modal.svelte"
    import {modals} from "./modals"

    export let title: string
    export let message: string

    const confirm = modals.confirm
</script>

{#if get(confirm).visible}
    <Modal>
        <h1>{title}</h1>
        {message}
        <button>OK</button>
        <button>Cancel</button>
    </Modal>
{/if}

<style>
    h1 {
        @apply text-center font-bold;
    }

    button {
        @apply border border-slate-600 rounded;
    }
</style>
