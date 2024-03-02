<script>
    export let personas
    let personasIndex = 0;
    let selectedPersona;

    $: selectedPersona = personas[personasIndex]

    /**
     * @param {number} number
     */
    function incrementPersonasIndex(number){
        personasIndex += number

        if(personasIndex < 0){
            personasIndex = personas.length - 1
        }
        if(personasIndex > personas.length - 1){
            personasIndex = 0
        }
    }

</script>


<div>
    <div>
        <h3>{selectedPersona?.name}</h3>
        <p>{selectedPersona?.description}</p>
        <img class="personaPortrait" alt={selectedPersona?.name} src={`public/portraits/${selectedPersona?.id}.png`}>
    </div>
    <div>
        <button on:click={() => { incrementPersonasIndex(-1) }}>
            <img src="public/rightarrow.png" alt="left arrow" class="arrowButton leftArrowImage">
        </button>
        <button on:click={() => { incrementPersonasIndex(1) }}>
            <img src="public/rightarrow.png" alt="right arrow" class="arrowButton">
        </button>
    </div>
</div>

<style>
    .arrowButton{
        height: 64px;
        width: 64px;
    }
    .leftArrowImage{
        transform: scaleX(-1);
    }
    .personaPortrait{
        width: 256px;
        height: 256px;
    }
</style>