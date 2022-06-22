import { PokemonProps } from 'types/Pokemon'
import styles from './PokemonCard.module.scss'

export default function PokemonCard({
	number,
	name,
	types,
	height,
	weight,
	sprite
}: PokemonProps) {
	return (
		<div className={ styles.PokemonCard }>
			<p>#{ number } { name }</p>

			<img src={ sprite } alt={ name } />

			<div className={ styles.content }>
				<p className={ styles.type }>{ types }</p>
				<p>HEIGHT: { height }</p>
				<p>WEIGHT: { weight }</p>
			</div>
		</div>
	)
}
