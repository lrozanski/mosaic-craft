module.exports = {
    root: true,
    extends: [
        "eslint:recommended",
        "plugin:@typescript-eslint/recommended",
    ],
    env: {
        browser: true,
        es6: true,
    },
    parserOptions: {
        ecmaVersion: "latest",
        sourceType: "module",
        ecmaFeatures: {
            jsx: true,
        },
        extraFileExtensions: [".svelte"],
    },
    parser: "@typescript-eslint/parser",
    plugins: [
        "@typescript-eslint",
        "svelte3",
        "tailwindcss",
    ],
    overrides: [
        {
            files: ["*.svelte"],
            processor: "svelte3/svelte3",
        },
    ],
    settings: {
        "svelte3/typescript": () => require("typescript"),
    },
    rules: {},
}
