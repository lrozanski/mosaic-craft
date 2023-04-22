<script lang="ts">
    import Icon from "@iconify/svelte"
    import FileUpload from "./FileUpload.svelte"
    import ConfirmModal from "./modal/ConfirmModal.svelte"
    import {tooltip} from "./stores"

    function addTooltip(element: Element) {
        element.addEventListener("mouseenter", e => tooltip.show((e.currentTarget as Element).getAttribute<string>("data-tooltip"), e.currentTarget as Element, {x: 0.5, y: -0.25}))
        element.addEventListener("mouseleave", () => tooltip.hide())
    }
</script>

<menu class="menu">
    <li class="icon" data-tooltip="Load Image" use:addTooltip>
        <FileUpload />
    </li>
    <li class="icon" data-tooltip="Select contours" use:addTooltip>
        <Icon icon="ic:outline-select-all" class="w-full h-full" />
    </li>
    <li class="icon" data-tooltip="Reset" use:addTooltip>
        <Icon icon="ic:outline-cancel" class="w-full h-full" />
    </li>
    <ConfirmModal title="Test" message="Test?" />
</menu>

<style>
    menu {
        @apply flex flex-col w-fit items-center p-1 mx-3 bg-slate-600 divide-y-2 divide-slate-500 rounded;
    }

    .icon {
        @apply w-10 h-10 p-2 text-slate-400 cursor-pointer hover:text-slate-50 transition-colors;
    }
</style>
