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


<div class="component">
    <h2>Your opponent:</h2>
    <div class="infoContainer">
        <h3 class="personaName">{selectedPersona?.name}</h3>
        <div class="description">{selectedPersona?.description}</div>
        <img class="personaPortrait" alt={selectedPersona?.name} src={`public/portraits/${selectedPersona?.id}.png`}>
        <div class="buttonsContainer">
            <button on:click={() => { incrementPersonasIndex(-1) }}>
                <img src="public/rightarrow.png" alt="left arrow" class="arrow leftArrowImage">
            </button>
            <button on:click={() => { incrementPersonasIndex(1) }}>
                <img src="public/rightarrow.png" alt="right arrow" class="arrow">
            </button>
        </div>
    </div>
</div>

<style>
    .arrow{
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
    button{
        border: none;
        background-color:transparent;
        cursor:grab;
    }
    .description{
        margin: 0px;
        height: 20%;
    }
    .component{
        display: flex;
        text-align: center;
        width: 40%;
        max-width: 40%;
        height: 100%;
        align-content: center;
        flex-direction:column;
        border: 1px solid brown;
    }
    .personaName{
        margin: 0px;
    }
    .buttonsContainer{
        position: absolute;
        bottom: 0;
        margin: auto;
    }
</style>