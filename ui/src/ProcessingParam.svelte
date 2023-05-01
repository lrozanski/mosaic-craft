<script lang="ts">
    import type {ChangeEventHandler} from "svelte/elements"

    export let type: string = "number"
    export let name: string
    export let label: string
    export let value: string
    export let min: number | undefined = undefined
    export let max: number | undefined = undefined
    export let step = 1
    export let updateParam: ChangeEventHandler<any>
</script>

<div class="grid grid-cols-12 gap-x-2 px-2 py-1">
    <label class="col-span-6 text-right" for="{name}">{label}:</label>
    <input class="param col-span-6" id="{name}" {type} name="{name}" value="{value}" min="{min}" max="{max}" step="{step}" required on:change="{updateParam}"
           autocomplete="off" />
<!--    <span class="col-span-2 text-center">{value}</span>-->
</div>

<style>
    .param {
        @apply bg-gray-700 rounded px-2 py-1;
    }
</style>
