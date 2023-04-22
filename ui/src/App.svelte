<script lang="ts">
    import Image from "./Image.svelte"
    import OptionsPanel from "./OptionsPanel.svelte"
    import Toolbar from "./Toolbar.svelte"
    import Tooltip from "./Tooltip.svelte"
</script>

<main>
    <Image />
    <Toolbar />
    <OptionsPanel />
</main>
<Tooltip />

<style>
    main {
        @apply flex flex-row items-center justify-center text-gray-400;
    }
</style>
