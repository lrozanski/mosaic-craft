<script lang="ts">
    import {afterUpdate} from "svelte"
    import {get} from "svelte/store"

    import {tooltip} from "./stores"

    let div: HTMLDivElement = null

    afterUpdate(() => {
        if (!div) {
            return
        }
        const {target, offset} = get(tooltip)
        const bounds = target.getBoundingClientRect()

        div.style.left = `calc(${bounds.right}px + ${offset?.x ?? 0}rem)`
        div.style.top = `calc(${bounds.top}px + ${offset?.y ?? 0}rem)`
    })
</script>

{#if $tooltip.visible}
    <div role="tooltip" class="tooltip" bind:this={div}>
        {$tooltip.text}
    </div>
{/if}

<style>
    .tooltip {
        @apply absolute flex flex-col justify-center p-3 text-slate-50 bg-gray-800 rounded select-none;
    }
</style>
