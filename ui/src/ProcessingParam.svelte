<script lang="ts">
    import type {ChangeEventHandler} from "svelte/elements"

    export let name: string
    export let label: string
    export let value: string
    export let min: number
    export let max: number
    export let updateParam: ChangeEventHandler<any>

    const range = (start: number, end: number) => Array.from({length: +end - start + 1}, (_, i) => +start + i)

    const datalistName = `datalist_${name}`
    const listItems = range(min, max)
    console.log(listItems)
</script>

<div class="grid grid-cols-12 gap-x-2 px-2 py-1">
    <label class="col-span-4 text-right">{label}:</label>
    <input class="col-span-7" id="num_clusters" type="range" name="{name}" value="{value}" min="{min}" max="{max}" step="1" required on:mousemove={updateParam}
           list="{datalistName}" />
    <datalist id="{datalistName}">
        {#each listItems as item}
            <option value="{item}" />
        {/each}
    </datalist>
    <span class="col-span-1 text-center">{value}</span>
</div>

<style>

</style>
