<template>
    <div class="error__count">
        <span class="resolved__count">
            Resolved: {{resolvedErrors}}
        </span>
        <span class="unresolved__count">
            Unresolved: {{unresolvedErrors}}
        </span>
        <span class="backlog__count">
            Backlog: {{backlogErrors}}
        </span>
    </div>
</template>

<script>

export default {
    props: ['resolvedErrors', 'unresolvedErrors', 'backlogErrors']
}
</script>
