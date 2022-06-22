import { useEffect, useState } from 'react'
import PokemonCard from 'components/PokemonCard'
import { PokemonProps } from 'types/Pokemon'
import styles from './App.module.scss'


export default function App() {
    const API_URL = process.env.REACT_APP_API_URL
    const [pokemons, setPokemons] = useState<PokemonProps[]>([])
    const [nextPage, setNextPage] = useState('')
    const [search, setSearch] = useState('')

    useEffect(() => {
        fetch(`${ API_URL }/api/pokemons/`)
        .then(response => response.json())
        .then(data => {
            setPokemons(data.results)
            setNextPage(data.next)
        })
    }, [])

    function handleSearch(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault()
        fetch(`${ API_URL }/api/pokemons/?search=${ search }`)
        .then(response => response.json())
        .then(data => {
            setPokemons(data.results)
            setNextPage(data.next)
        })
    }

    function seeMore() {
        fetch(nextPage)
        .then(response => response.json())
        .then(data => {
            // console.log(nextPage, data)
            setPokemons([...pokemons, ...data.results])
            setNextPage(data.next)
        })
    }

    return (
        <div className={ styles.App }>
            <div className={ styles.bannerContainer }>
                <img className={ styles.banner }
                    src="/assets/images/banner.png"
                    alt="PokeApi Logo"
                />

                <form onSubmit={ event => handleSearch(event) }>
                    <input
                        type="text"
                        placeholder="Search..."
                        onChange={ event => setSearch(event.target.value) }
                        value={ search }
                    />
                    <button type="submit">GO</button>
                </form>

            </div>

            <section className={ styles.menu }>
                { pokemons.map(pokemon => (
                    <PokemonCard
                        key={ pokemon.number }
                        {...pokemon}
                    />
                ))}
            </section>

            { nextPage && (
                <div className={ styles.nextPage }>
                    <button onClick={ seeMore }>
                        See more
                    </button>
                </div>
			)}

            <footer>
                <p className={ styles.footerText }>
                    Feito com carinho por quem entende de Pokémon!!
                </p>
            </footer>
        </div>
    )
}
