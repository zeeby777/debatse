<script>
    import { onMount } from 'svelte';

    let personas = [];
    let personasIndex = 0;

    onMount(async () => {
		const res = await fetch(`http://localhost:5000/debater_personas_index`, {
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
            }
        });
		const json = await res.json();
        console.log(json)
	});

    $: console.log(personasIndex)
</script>

<html lang="en">
    <style src="style.css"></style>
    <div class="modal">
        <h1>DEBATSE</h1>
        <p>This is a game where you debate an unhinged AI, and get judged by an unhinged AI also. This simulates most online discourse in 2024.</p>

        <!-- Selector -->
        <div>
            <div>
                {personas[personasIndex]}
            </div>
            <button on:click={() => { personasIndex--}}>
                <img src="public/rightarrow.png" alt="right arrow" class="arrowButton leftArrowImage">
            </button>
            <button on:click={() => { personasIndex++}}>
                <img src="public/rightarrow.png" alt="right arrow" class="arrowButton">
            </button>
        </div>
    </div>
</html>

<style>
.arrowButton{
    height: 64px;
    width: 64px;
}
.leftArrowImage{
    transform: scaleX(-1);
}
</style>