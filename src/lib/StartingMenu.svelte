<script>
    import { onMount } from 'svelte';
    import OpponentSelector from './OpponentSelector.svelte';

    let personas = [];
    let personasIndex = 0;

    onMount(async () => {
		const res = await fetch(`http://localhost:5000/debater_personas_index`, {
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
            },
            
        });
		personas = await res.json();
	});

    $: console.log(personas)
</script>

<html lang="en">
    <style src="style.css"></style>
    <div class="modal">
        <h1>DEBATSE</h1>
        <p>This is a game where you debate an unhinged AI, and get judged by an unhinged AI also. This simulates most online discourse in 2024.</p>

        <OpponentSelector {personas}/>
    </div>
</html>

<style>
</style>