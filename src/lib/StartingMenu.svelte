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
        <h1 class="">DEBATSE</h1>
        <p class="anta-regular">This is a game where you debate an unhinged AI, and get judged by an unhinged AI also. This simulates most online discourse in 2024.</p>
        <hr>

        <OpponentSelector {personas}/>
    </div>
</html>

<style>
    .modal{
        display: flex;
        flex-direction: column;
        border: 1px solid black;
        width: 50%;
        height: 50%;
        text-align:center;
        position: absolute;
        top: 50%;  /* position the top  edge of the element at the middle of the parent */
        left: 50%; /* position the left edge of the element at the middle of the parent */
        transform: translate(-50%, -50%); /* This is a shorthand of
                                            translateX(-50%) and translateY(-50%) */
    }
</style>