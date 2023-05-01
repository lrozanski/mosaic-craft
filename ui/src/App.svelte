<script lang="ts">
    import Image from "./Image.svelte"
    import ImageToolbar from "./ImageToolbar.svelte"
    import OptionsPanel from "./OptionsPanel.svelte"
    import Toolbar from "./Toolbar.svelte"
    import Tooltip from "./Tooltip.svelte"
</script>

<main>
    <div class="flex flex-col items-center">
        <Image />
        <ImageToolbar />
    </div>
    <Toolbar />
    <OptionsPanel />
</main>
<Tooltip />

<style>
    main {
        @apply flex flex-row items-center justify-center text-gray-300;
    }
</style>
